import json

HEADERS = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Headers': '*',
    'Access-Control-Allow-Methods': 'POST, OPTIONS'
}

def lambda_handler(event, context):
    method = event.get('requestContext', {}).get('http', {}).get('method', '')
    
    if method == 'OPTIONS':
        return {'statusCode': 200, 'headers': HEADERS, 'body': ''}
    
    try:
        body = json.loads(event.get('body', '{}'))
    except:
        body = {}
    
    text = body.get('text', '')
    
    positive = ['good','great','happy','excellent',
                'love','amazing','awesome','fantastic']
    negative = ['bad','terrible','sad','hate',
                'poor','worst','awful']
    
    text_lower = text.lower()
    pos = sum(1 for w in positive if w in text_lower)
    neg = sum(1 for w in negative if w in text_lower)
    
    if pos > neg:
        sentiment = 'POSITIVE'
    elif neg > pos:
        sentiment = 'NEGATIVE'
    else:
        sentiment = 'NEUTRAL'
    
    return {
        'statusCode': 200,
        'headers': HEADERS,
        'body': json.dumps({
            'text': text,
            'sentiment': sentiment
        })
    }