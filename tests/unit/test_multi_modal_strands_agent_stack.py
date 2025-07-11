import aws_cdk as core
import aws_cdk.assertions as assertions

from multi_modal_strands_agent.multi_modal_strands_agent_stack import MultiModalStrandsAgentStack

# example tests. To run these tests, uncomment this file along with the example
# resource in multi_modal_strands_agent/multi_modal_strands_agent_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = MultiModalStrandsAgentStack(app, "multi-modal-strands-agent")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
