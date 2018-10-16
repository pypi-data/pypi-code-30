from flask import Flask, jsonify, request, send_from_directory
from importlib import import_module

import json
import os
import requests
import uuid

def generate_app(config=None):
	__DefaultConfig = {
		"DBConnection": "DictConnection",
		"DBParameters": [],
		"AllowedActions": [
			"addData",
			"addTopic",
			"getData",
			"getSummary",
			"getTopics",
			"getTopic"
		],
		"ServeCWD": True
	}

	__InvalidTokenJSON = {
		"error": "Token not recognized"
	}

	__ActionNotAllowedJSON = {
		"error": "Action not allowed"
	}

	if not config:
		__config = __DefaultConfig
	elif type(config) == str:
		with open(filename, "r") as f:
			__config = json.load(f)
	elif type(config) != dict:
		raise  ValueError("Input configuration not recognized.")

	# TODO: static files
	APP = Flask(__name__, static_folder=os.path.join(os.getcwd(), "static"))

	__DBConnectionMod = import_module("fdbk." + __config["DBConnection"])
	__DBConnection = __DBConnectionMod.ConnectionClass(*(__config["DBParameters"]))

	# API

	if __config["ServeCWD"]:
		@APP.route('/')
		def index():
			return send_from_directory(os.getcwd(), 'index.html')

	@APP.route('/add/topic', methods=["POST"])
	def addTopic():
		if "addTopic" not in __config["AllowedActions"]:
			return jsonify(__ActionNotAllowedJSON), 403
		if "AddTokens" in __config and __config["AddTokens"] and ("token" not in request.args or request.args["token"] not in __config["AddTokens"]):
			return jsonify(__InvalidTokenJSON), 403
		try:
			json_in = request.get_json()
		except:
			return jsonify({
				"error": "No topic data provided in request"
			}), 404

		topic = json_in.pop("topic", None)
		if not topic:
			return jsonify({
				"error": "No 'topic' field in input data"
			}), 404

		try:
			__DBConnection.addTopic(topic, **json_in)
		except KeyError as e:
			# Field not available in input data
			return jsonify({
				"error": str(e)
			}), 404
		except TypeError as e:
			return jsonify({
				"error": str(e)
			}), 400
		return jsonify({
			"success": "Data successfully added to DB"
		})

	@APP.route('/add/data/<topic>', methods=["POST"])
	def addData(topic):
		if "addData" not in __config["AllowedActions"]:
			return jsonify(__ActionNotAllowedJSON), 403
		if "AddTokens" in __config and __config["AddTokens"] and ("token" not in request.args or request.args["token"] not in __config["AddTokens"]):
			return jsonify(__InvalidTokenJSON), 403
		try:
			if not __DBConnection.getTopic(topic)["allow_api_submissions"]:
				return jsonify({
					"error": "Data submissions through API not allowed for topic '" + topic + "'"
				}), 403
		except KeyError as e:
			# Topic not defined
			return jsonify({
				"error": str(e)
			}), 404

		try:
			json_in = request.get_json()
		except:
			return jsonify({
				"error": "No topic data provided in request"
			}), 404
		try:
			__DBConnection.addData(topic, json_in)
		except KeyError as e:
			# Topic not defined
			return jsonify({
				"error": str(e)
			}), 404
		except ValueError as e:
			# Fields do not match with topic
			return jsonify({
				"error": str(e)
			}), 400
		return jsonify({
			"success": "Data successfully added to DB"
		})

	@APP.route('/get/topics', methods=["GET"])
	def getTopics():
		if "getTopics" not in __config["AllowedActions"]:
			return jsonify(__ActionNotAllowedJSON), 403
		return jsonify(__DBConnection.getTopics())

	@APP.route('/get/topic/<topic>', methods=["GET"])
	def getTopic(topic):
		if "getTopic" not in __config["AllowedActions"]:
			return jsonify(__ActionNotAllowedJSON), 403
		try:
			topic_json = __DBConnection.getTopic(topic)
			return jsonify(topic_json)
		except KeyError as e:
			return jsonify({
				"error": str(e)
			}), 404

	@APP.route('/get/data/<topic>', methods=["GET"])
	def getData(topic):
		if "getData" not in __config["AllowedActions"]:
			return jsonify(__ActionNotAllowedJSON), 403
		try:
			data = __DBConnection.getData(topic)
			return jsonify(data)
		except KeyError as e:
			return jsonify({
				"error": str(e)
			}), 404


	@APP.route('/get/summary/<topic>', methods=["GET"])
	def getSummary(topic):
		if "getSummary" not in __config["AllowedActions"]:
			return jsonify(__ActionNotAllowedJSON), 403
		try:
			data = __DBConnection.getSummary(topic)
			return jsonify(data)
		except KeyError as e:
			return jsonify({
				"error": str(e)
			}), 404

	return APP
