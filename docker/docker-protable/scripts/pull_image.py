import os
import common
import requests

def pull_image(repo, version='latest'):
    registry_repo = common.registry_url + '/' + repo + ':' + version
    os.system('docker pull ' + registry_repo)
    os.system('docker tag ' + registry_repo + ' ' + repo)
    os.system('docker rmi -f ' + registry_repo)
    
def pull_all_registry_images():
    x = requests.get('http://' + common.registry_url + '/v2/_catalog')
    for reponame in x.json()['repositories']:
        y = requests.get('http://' + common.registry_url + '/v2/' + reponame + '/tags/list')
        for v in y.json()['tags']:
            # print(reponame, v)
            pull_image(reponame, v)


def test():
    # print('something')
    pull_all_registry_images()
    
test()