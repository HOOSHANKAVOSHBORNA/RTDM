import os
import common

def push_image(repo):
    owned_repo = common.registry_url + '/' + repo
    if not common.registry_url in repo:
        os.system('docker tag ' + repo + ' ' + owned_repo)
    
    os.system('docker push ' + owned_repo)
    
    
def push_all_existing_images():
    file_name = 'docker-images.txt'
    os.system("docker images --format '{{.Repository}}' > " + file_name)
    f = open(file_name, 'r+')
    ls = f.readlines()
    for l in ls:
        push_image(l.replace('\n', ''))


def test():
    print('something')
    
    
test()