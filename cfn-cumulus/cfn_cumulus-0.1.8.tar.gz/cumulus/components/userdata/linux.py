from troposphere import (
    Ref,
    Join,
)


def user_data_for_cfn_init(launch_config_name, asg_name, configsets):
    """
    :return: A troposphere Join object that contains userdata for use with cfn-init

    :param configsets: The single 'key' value set in the cfn-init Metadata parameter: cloudformation.InitConfigSets
    :type asg_name: String name of the ASG cloudformation resource
    :type launch_config_name: String name of the launch config cloudformation resource
    """
    default_userdata_asg_signal = (
        Join('',
             [
                 "#!/bin/bash -xe\n",
                 "yum update aws-cfn-bootstrap\n",
                 "# Install the files and packages from the metadata\n",
                 "/opt/aws/bin/cfn-init ",
                 "         --stack ", Ref("AWS::StackName"),
                 "         --resource ", launch_config_name,
                 "         --configsets %s " % configsets,
                 "         --region ", Ref("AWS::Region"), "\n",
                 # "# Get exit code of cfn init to use in cfn-signal\n",
                 # "export init_status=$?", "\n"
                 # Signal regardless of existence of an update policy.
                 # An error will pop up in the logs but I don't think this causes a problem.
                 "# Signal the ASG we are ready\n\n",
                 "/opt/aws/bin/cfn-signal -e 0",
                 # "/opt/aws/bin/cfn-signal -e $init_status",
                 "    --resource %s" % asg_name,
                 "    --stack ", Ref("AWS::StackName"),
                 "    --region ", Ref("AWS::Region"),
                 "\n"
             ]))
    return default_userdata_asg_signal
