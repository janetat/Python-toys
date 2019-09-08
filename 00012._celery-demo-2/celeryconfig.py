broker_url = 'amqp://'

result_backend = 'redis://localhost:6379/1'

imports = ['tasks.math', 'tasks.download']

task_publish_retry_policy = {
    'max_retries': 3,
    'interval_start': 0,
    'interval_step': 0.2,
    'interval_max': 0.2
}

task_queues = {
    'add': {
        'routing_key': 'add'
    },
    'download': {
        'exchange': 'media',
        'routing_key': 'download'
    }
}

task_routes = {
    'tasks.math.add': {
        'queue': 'add',
        'routing_key': 'add',
        'serializer': 'json',
    },
    'tasks.download.download_img': {
        'queue': 'download',
        'routing_key': 'download'
    }
}