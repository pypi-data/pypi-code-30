import logging
import pika

log = logging.getLogger(__name__)


class BaseConsumer(object):
    """
    BaseConsumer will handle unexpected interactions with RabbitMQ such as channel and connection closures.

    If RabbitMQ closes the connection, it will reopen it. You should
    look at the output, as there are limited reasons why the connection may
    be closed, which usually are tied to permission related issues or
    socket timeouts.
    If the channel is closed, it will indicate a problem with one of the
    commands that were issued and that should surface in the output as well.
    """

    def __init__(self, amqp_url):
        """
        Create a new instance of the consumer class, passing in the AMQP URL used to connect to RabbitMQ.

        :param str amqp_url: The AMQP url to connect with
        """
        self._connection = None
        self._channel = None
        self._closing = False
        self._consumer_tag = None
        self._url = amqp_url

        self._queue = ''
        self._on_message_callback = None   # Use a callback to process the message.
        self._message_count = 0            # Count messages and failed messages.
        self._failed_message_count = 0

        self._exchange_name = ''
        self._exchange_type = 'direct'
        self._routing_key = ''

    def set_queue(self, routing_key, queue=''):
        self._routing_key = routing_key
        self._queue = queue

    def set_exchange(self, exchange_name, exchange_type='direct'):
        self._exchange_name = exchange_name
        self._exchange_type = exchange_type

    def add_on_message_callback(self, on_message_callback):
        self._on_message_callback = on_message_callback

    def connect(self):
        """
        Connect to RabbitMQ, returning the connection handle.

        When the connection is established, the on_connection_open method
        will be invoked by pika.
        :rtype: pika.SelectConnection
        """
        log.info('Connecting to %s', self._url)
        return pika.SelectConnection(pika.URLParameters(self._url),
                                     self.on_connection_open,
                                     self.on_connection_error,   # !! Handle error opening connection
                                     stop_ioloop_on_close=False)

    def on_connection_open(self, unused_connection):
        """
        Call by pika once the connection to RabbitMQ has been established.

        It passes the handle to the connection object in
        case we need it, but in this case, we'll just mark it unused.
        :type unused_connection: pika.SelectConnection
        """
        log.info('Connection opened')
        self.add_on_connection_close_callback()
        self.open_channel()

    def on_connection_error(self, unused_connection, message):
        """
        Call by pika if the connection to RabbitMQ has failed to be established.

        It passes the handle to the connection object in
        case we need it, but in this case, we'll just mark it unused.
        :type unused_connection: pika.SelectConnection
        """
        log.error('Connection failed, closing: %s', message)
        self.stop()

    def add_on_connection_close_callback(self):
        """Add on close callback, invoked when RabbitMQ closes the connection to the publisher unexpectedly."""
        log.info('Adding connection close callback')
        self._connection.add_on_close_callback(self.on_connection_closed)

    def on_connection_closed(self, connection, reply_code, reply_text):
        """
        Invoke by pika when the connection to RabbitMQ is closed unexpectedly.

        Since it is unexpected, we will reconnect to RabbitMQ if it disconnects.
        :param pika.connection.Connection connection: The closed connection obj
        :param int reply_code: The server provided reply_code if given
        :param str reply_text: The server provided reply_text if given
        """
        self._channel = None
        if self._closing:
            self._connection.ioloop.stop()
        else:
            log.warning('Connection closed, reopening in 5 seconds: (%s) %s', reply_code, reply_text)
            self._connection.add_timeout(5, self.reconnect)

    def reconnect(self):
        """
        Will be invoked by the IOLoop timer if the connection is closed.

        See the on_connection_closed method.
        """
        # This is the old connection IOLoop instance, stop its ioloop
        self._connection.ioloop.stop()

        if not self._closing:

            # Create a new connection
            self._connection = self.connect()

            # There is now a new connection, needs a new ioloop to run
            self._connection.ioloop.start()

    def open_channel(self):
        """
        Open a new channel with RabbitMQ by issuing the Channel.

        Open RPC command. When RabbitMQ responds that the channel is open, the
        on_channel_open callback will be invoked by pika.
        """
        log.info('Creating a new channel')
        self._connection.channel(on_open_callback=self.on_channel_open)

    def on_channel_open(self, channel):
        """
        Invoke by pika when the channel has been opened.

        The channel object is passed in so we can make use of it.
        Since the channel is now open, we'll declare the exchange to use.
        :param pika.channel.Channel channel: The channel object
        """
        log.info('Channel opened')
        self._channel = channel
        self.add_on_channel_close_callback()
        self.setup_exchange(self._exchange_name)

    def add_on_channel_close_callback(self):
        """Tells pika to call the on_channel_closed method if RabbitMQ unexpectedly closes the channel."""
        log.info('Adding channel close callback')
        self._channel.add_on_close_callback(self.on_channel_closed)

    def on_channel_closed(self, channel, reply_code, reply_text):
        """
        Invoke by pika when RabbitMQ unexpectedly closes the channel.

        Channels are usually closed if you attempt to do something that
        violates the protocol, such as re-declare an exchange or queue with
        different parameters. In this case, we'll close the connection
        to shutdown the object.
        :param pika.channel.Channel: The closed channel
        :param int reply_code: The numeric reason the channel was closed
        :param str reply_text: The text reason the channel was closed
        """
        log.warning('Channel %i was closed: (%s) %s', channel, reply_code, reply_text)
        self._connection.close()

    def setup_exchange(self, exchange_name):
        """
        Start the exchange on RabbitMQ by invoking the Exchange.Declare RPC command.

        When it is complete, the on_exchange_declareok method will be invoked by pika.
        :param str|unicode exchange_name: The name of the exchange to declare
        """
        log.info('Declaring exchange %s', exchange_name)
        self._channel.exchange_declare(self.on_exchange_declareok,
                                       exchange_name,
                                       self._exchange_type)

    def on_exchange_declareok(self, unused_frame):
        """
        Invoke by pika when RabbitMQ has finished the Exchange.Declare RPC command.

        :param pika.Frame.Method unused_frame: Exchange.DeclareOk response frame
        """
        log.info('Exchange declared')
        self.setup_queue(self._queue)

    def setup_queue(self, queue_name):
        """
        Start the queue on RabbitMQ by invoking the Queue.Declare RPC command.

        When it is complete, the on_queue_declareok method will be invoked by pika.
        :param str|unicode queue_name: The name of the queue to declare.
        """
        log.info('Declaring queue %s', queue_name)
        if len(queue_name) > 0:
            self._channel.queue_declare(self.on_queue_declareok, queue_name)
        else:
            self._channel.queue_declare(self.on_queue_declareok, exclusive=True)

    def on_queue_declareok(self, method_frame):
        """
        Invoke by pika when the Queue.Declare RPC call made in setup_queue has completed.

        In this method we will bind the queue and exchange together with the routing key by issuing the Queue.Bind
        RPC command. When this command is complete, the on_bindok method will
        be invoked by pika.
        :param pika.frame.Method method_frame: The Queue.DeclareOk frame
        """
        log.info('Binding %s to %s with %s', self._exchange_name, self._queue, self._routing_key)
        self._channel.queue_bind(self.on_bindok, self._queue,
                                 self._exchange_name, self._routing_key)

    def on_bindok(self, unused_frame):
        """
        Invoke by pika when the Queue.Bind method has completed.

        At this point we will start consuming messages by calling start_consuming
        which will invoke the needed RPC commands to start the process.
        :param pika.frame.Method unused_frame: The Queue.BindOk response frame
        """
        log.info('Queue bound')
        self.start_consuming()

    def start_consuming(self):
        """
        start_consuming sets up the consumer.

        Done by first calling add_on_cancel_callback so that the object is notified if RabbitMQ
        cancels the consumer. It then issues the Basic.Consume RPC command
        which returns the consumer tag that is used to uniquely identify the
        consumer with RabbitMQ. We keep the value to use it when we want to
        cancel consuming. The on_message method is passed in as a callback pika
        will invoke when a message is fully received.
        """
        log.info('Issuing consumer related RPC commands')
        self.add_on_cancel_callback()
        self._consumer_tag = self._channel.basic_consume(self.on_message,
                                                         self._queue)

    def add_on_cancel_callback(self):
        """
        Add a callback that will be invoked if RabbitMQ cancels the consumer for some reason.

        If RabbitMQ does cancel the consumer, on_consumer_cancelled will be invoked by pika.
        """
        log.info('Adding consumer cancellation callback')
        self._channel.add_on_cancel_callback(self.on_consumer_cancelled)

    def on_consumer_cancelled(self, method_frame):
        """
        Invoke by pika when RabbitMQ sends a Basic.Cancel for a consumer receiving messages.

        :param pika.frame.Method method_frame: The Basic.Cancel frame
        """
        log.info('Consumer was cancelled remotely, shutting down: %r', method_frame)
        if self._channel:
            self._channel.close()

    def on_message(self, unused_channel, basic_deliver, properties, body):
        """
        Invoke by pika when a message is delivered from RabbitMQ.

        The channel is passed for your convenience. The basic_deliver object that
        is passed in carries the exchange, routing key, delivery tag and
        a redelivered flag for the message. The properties passed in is an
        instance of BasicProperties with the message properties and the body
        is the message that was sent.
        :param pika.channel.Channel unused_channel: The channel object
        :param pika.Spec.Basic.Deliver: basic_deliver method
        :param pika.Spec.BasicProperties: properties
        :param str|unicode body: The message body
        """
        log.info('Received message # %s from %s: %s', basic_deliver.delivery_tag, properties.app_id, body)

        acknowledge_this_message = True
        if self._on_message_callback:
            try:
                self._on_message_callback(body)
            except Exception:
                acknowledge_this_message = False

        self._message_count = self._message_count + 1
        if acknowledge_this_message:
            self.acknowledge_message(basic_deliver.delivery_tag)
        else:
            self._failed_message_count = self._failed_message_count + 1
            self.reject_message(basic_deliver.delivery_tag)
        log.info('Processed %d messages. %d failed messages', self._message_count, self._failed_message_count)

    def acknowledge_message(self, delivery_tag):
        """
        Acknowledge the message delivery from RabbitMQ by sending a Basic.Ack RPC method for the delivery tag.

        :param int delivery_tag: The delivery tag from the Basic.Deliver frame
        """
        log.info('Acknowledging message %s', delivery_tag)
        self._channel.basic_ack(delivery_tag)

    def reject_message(self, delivery_tag):
        """
        Reject the message delivery from RabbitMQ by sending a Basic.Nack RPC method for the delivery tag.

        :param int delivery_tag: The deliver tag from Basic.Deliver frame
        """
        log.info('Reject message %s', delivery_tag)
        self._channel.basic_nack(delivery_tag)

    def stop_consuming(self):
        """Tell RabbitMQ that you would like to stop consuming by sending the Basic.Cancel RPC command."""
        if self._channel:
            log.info('Sending a Basic.Cancel RPC command to RabbitMQ')
            self._channel.basic_cancel(self.on_cancelok, self._consumer_tag)

    def on_cancelok(self, unused_frame):
        """
        on_cancelok is invoked by pika when RabbitMQ acknowledges the cancellation of a consumer.

        At this point we will close the channel.
        This will invoke the on_channel_closed method once the channel has been
        closed, which will in-turn close the connection.
        :param pika.frame.Method unused_frame: The Basic.CancelOk frame
        """
        log.info('RabbitMQ acknowledged the cancellation of the consumer')
        self.close_channel()

    def close_channel(self):
        """
        Call to close the channel with RabbitMQ.

        Close cleanly by issuing the Channel.Close RPC command.
        """
        log.info('Closing the channel')
        self._channel.close()

    def run(self):
        """
        Run the consumer by connecting to RabbitMQ.

        Then start the IOLoop to block and allow the SelectConnection to operate.
        """
        self._connection = self.connect()
        self._connection.ioloop.start()

    def stop(self):
        """
        Clean shutdown the connection to RabbitMQ by stopping the consumer with RabbitMQ.

        When RabbitMQ confirms the cancellation, on_cancelok
        will be invoked by pika, which will then closing the channel and
        connection. The IOLoop is started again because this method is invoked
        when CTRL-C is pressed raising a KeyboardInterrupt exception. This
        exception stops the IOLoop which needs to be running for pika to
        communicate with RabbitMQ. All of the commands issued prior to starting
        the IOLoop will be buffered but not processed.
        """
        log.info('Stopping')
        log.info('Processed %d messages. %d failed messages', self._message_count, self._failed_message_count)
        self._closing = True
        self.stop_consuming()
        self._connection.ioloop.stop()
        log.info('Stopped')

    def close_connection(self):
        """close_connection method closes the connection to RabbitMQ."""
        log.info('Closing connection')
        self._connection.close()
