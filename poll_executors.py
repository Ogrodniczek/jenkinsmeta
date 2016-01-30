import requests
#use https://requests-cache.readthedocs.org/en/latest/index.html instead of that dirty decorator

host='localhost:8080'
'http://localhost:8080/view/kekekeke/api/json?pretty=true'
'http://localhost:8080/computer/api/json?pretty=true'


def executors(host):
    return requests.get('http://'+host+'/computer/api/json?pretty=true').json()['computer']


def queue(host):
    return requests.get('http://'+host+'/queue/api/json?pretty=true').json()['items']

def views(host):
    return requests.get('http://'+host+'/api/json?pretty=true').json()['views']


def jobs(host):
    return requests.get('http://'+host+'/api/json?pretty=true').json()['jobs']


def get_last_build(host, job):
    return str(requests.get('http://'+host+'/job/'+job+'/api/json?pretty=true').json()['lastBuild']['number'])


def get_executor_for_job(host, job, number):
    return requests.get('http://'+host+'/job/'+job+'/'+number+'/api/json?pretty=true').json()['builtOn']



def build_executors_info():
    jobs_on_executors={}
    result = {}
    for job in jobs(host):
        last_build = get_last_build(host, job['name'])
        jobs_on_executors[get_executor_for_job(host, job['name'], last_build)] = job, last_build
    for computer in executors(host):
        ###if master then empty
        jobs_on_executor = []
        if computer['displayName'] in jobs_on_executors:
            jobs_on_executor.append(jobs_on_executors[computer['displayName']])
        result[computer['displayName']]= computer['numExecutors'], computer['offline'], jobs_on_executor
    return result


print('####')
#print(views(host))
#print(jobs(host))
#print(executors(host))
def build_queue_info():
    for item in queue(host):
        #'id' needed to cancel item -> http://localhost:8080/queue/cancelItem?id=5
        #'why' as popup
        print(item['task']['name'])

print(build_executors_info())
#build_queue_info()
