import boto3
alb_client = boto3.client('elbv2',"us-east-1")
list_of_regions=['ap-south-1','eu-west-3','eu-west-2','eu-west-1','sa-east-1','ap-southeast-1','ap-southeast-2','eu-central-1','us-east-1','us-east-2','us-west-1','us-west-2']
albs = alb_client.describe_load_balancers()
for alb in albs['LoadBalancers']:
    # listeners = alb_client.describe_listeners(
    #     LoadBalancerArn=alb['LoadBalancerArn']
    # )
    response = alb_client.describe_target_groups(
        LoadBalancerArn=alb['LoadBalancerArn']
    )
    try:
        print("Checking target groups for NLB-", alb['LoadBalancerArn'].split("net/")[1].split("/")[0])

    except Exception as ex:
        print("Checking target groups for ALB-", alb['LoadBalancerArn'].split("app/")[1].split("/")[0])
    # print(target_group)
    for target_group in response['TargetGroups']:
        targets = alb_client.describe_target_health(
            TargetGroupArn=target_group['TargetGroupArn']
        )
        if targets['TargetHealthDescriptions']:
            print("  targets are"+str(targets))
    #     if "ip" in target_group:
    #         print("   Target group with no instance- "+target_group['TargetGroupName'])