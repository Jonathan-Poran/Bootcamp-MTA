import json

def lambda_handler(event, context):
    print("event = ", event)
    try:
        num1 = float(event['queryStringParameters']['num1'])
        num2 = float(event['queryStringParameters']['num2'])
        operation = event['queryStringParameters']['operation']
        print('num1 = ', num1, ", num2 = ", num2, ", operation = ", operation)

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                return {
                    'statusCode': 400,
                    'headers': {
                        'Access-Control-Allow-Origin': '*'
                    },
                    'body': json.dumps({'error': 'Division by zero is not allowed'})
                }
            result = num1 / num2
        else:
            return {
                'statusCode': 400,
                'headers': {
                    'Access-Control-Allow-Origin': '*'
                },
                'body': json.dumps({'error': 'Invalid operation'})
            }

        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'result': result})
        }

    except (KeyError, TypeError, ValueError) as e:
        return {
            'statusCode': 400,
            'headers': {
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'error': f'Invalid input: {str(e)}'})
        }
