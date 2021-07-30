"""
A module for obtaining repo readme and language data from the github API.
Before using this module, read through it, and follow the instructions marked
TODO.
After doing so, run it like this:
    python acquire.py
To create the `data.json` file that contains the data.
"""
import os
import json
from typing import Dict, List, Optional, Union, cast
import requests
import pandas as pd

from env import github_token, github_username

# TODO: Make a github personal access token.
#     1. Go here and generate a personal access token https://github.com/settings/tokens
#        You do _not_ need select any scopes, i.e. leave all the checkboxes unchecked
#     2. Save it in your env.py file under the variable `github_token`
# TODO: Add your github username to your env.py file under the variable `github_username`
# TODO: Add more repositories to the `REPOS` list below.

REPOS = ['/awesome-selfhosted/awesome-selfhosted',
 '/jaywcjlove/awesome-mac',
 '/goabstract/Awesome-Design-Tools',
 '/viatsko/awesome-vscode',
 '/ascoders/weekly',
 '/davidsonfellipe/awesome-wpo',
 '/shekhargulati/52-technologies-in-2016',
 '/hackerkid/Mind-Expanding-Books',
 '/apsdehal/awesome-ctf',
 '/imfunniee/gitfolio',
 '/Kristories/awesome-guidelines',
 '/swapagarwal/swag-for-dev',
 '/cezaraugusto/You-Dont-Know-JS',
 '/stackshareio/awesome-stacks',
 '/vitejs/awesome-vite',
 '/jdorfman/awesome-json-datasets',
 '/huyingjie/Checklist-Checklist',
 '/stefanbuck/awesome-browser-extensions-for-github',
 '/wubaiqing/zaobao',
 '/f2e-awesome/knowledge',
 '/soroushchehresa/awesome-coronavirus',
 '/t9tio/open-source-jobs',
 '/metrofun/machine-learning-surveys',
 '/yangshun/awesome-spinners',
 '/junosuarez/awesome-npx',
 '/sergey-pimenov/awesome-web-animation',
 '/philsturgeon/awesome-earth',
 '/diegohaz/awesome-react-context',
 '/ElaWorkshop/awesome-cn-cafe',
 '/jagracey/Awesome-Unicode',
 '/vinta/awesome-python',
 '/521xueweihan/HelloGitHub',
 '/lauris/awesome-scala',
 '/lk-geimfari/awesomo',
 '/wilsonfreitas/awesome-quant',
 '/PaddlePaddle/PaddleHub',
 '/detailyang/awesome-cheatsheet',
 '/chrissimpkins/codeface',
 '/ml-tooling/best-of-ml-python',
 '/paralax/awesome-honeypots',
 '/likedan/Awesome-CoreML-Models',
 '/yzhao062/anomaly-detection-resources',
 '/rossant/awesome-math',
 '/0xInfection/Awesome-WAF',
 '/INTERMT/Awesome-PyTorch-Chinese',
 '/dahlia/awesome-sqlalchemy',
 '/Separius/awesome-sentence-embedding',
 '/xxh/xxh',
 '/fendouai/Awesome-Chatbot',
 '/ml-tooling/best-of-python',
 '/wxWidgets/Phoenix',
 '/kaxap/arl',
 '/springload/awesome-wagtail',
 '/ml-tooling/best-of-web-python',
 '/fendouai/Awesome-TensorFlow-Chinese',
 '/anmol098/waka-readme-stats',
 '/ucg8j/awesome-dash',
 '/mhxion/awesome-discord-communities',
 '/florimondmanca/awesome-asgi',
 '/applicable-ml/awesome-ml-demos-with-ios',
 '/docker/awesome-compose',
 '/terkelg/awesome-creative-coding',
 '/PatrickJS/awesome-angular',
 '/webpack-contrib/awesome-webpack',
 '/ipfs/awesome-ipfs',
 '/samber/awesome-prometheus-alerts',
 '/krishnakumarsekar/awesome-quantum-machine-learning',
 '/hookmaster/frida-all-in-one',
 '/kujian/frontendDaily',
 '/lyfeyaj/awesome-resources',
 '/EliotAndres/kaggle-past-solutions',
 '/rootsongjc/awesome-cloud-native',
 '/zhengxiaopeng/android-dev-bookmarks',
 '/ITI/ICS-Security-Tools',
 '/liyupi/free-programming-resources',
 '/geek-cookbook/geek-cookbook',
 '/theNewDynamic/awesome-hugo',
 '/acgeospatial/awesome-earthobservation-code',
 '/krzemienski/awesome-video',
 '/awesome-br/awesome-br.github.io',
 '/aliesbelik/awesome-jmeter',
 '/unchase/awesome-russian-it',
 '/wardley-maps-community/awesome-wardley-maps',
 '/csinva/csinva.github.io',
 '/ligurio/awesome-ttygames',
 '/posquit0/hugo-awesome-identity',
 '/ayr-ton/awesome-geek-podcasts',
 '/overnote/awesome-kubernetes-notes',
 '/faridrashidi/kaggle-solutions',
 '/planetruby/conferences',
 '/sindresorhus/awesome',
 '/papers-we-love/papers-we-love',
 '/unixorn/awesome-zsh-plugins',
 '/thibmaek/awesome-raspberry-pi',
 '/k4m4/movies-for-hackers',
 '/skywind3000/awesome-cheatsheets',
 '/ashishb/android-security-awesome',
 '/awesome-lists/awesome-bash',
 '/frenck/awesome-home-assistant',
 '/chubin/awesome-console-services',
 '/jghoman/awesome-apache-airflow',
 '/zudochkin/awesome-newsletters',
 '/aviaryan/awesome-no-login-web-apps',
 '/ashishb/osx-and-ios-security-awesome',
 '/CompSciLauren/awesome-git-hooks',
 '/RichardLitt/awesome-styleguides',
 '/jeffreytse/zsh-vi-mode',
 '/sroberts/awesome-iocs',
 '/aitemr/awesome-git-hooks',
 '/jhermann/awesome-python-talks',
 '/dennyzhang/cheatsheet.dennyzhang.com',
 '/makccr/dot',
 '/calee0219/awesome-5g',
 '/MorganGeek/bookmarks',
 '/HongxuChen/awesome-llvm',
 '/buren/awesome-sweden',
 '/jeffreytse/jekyll-deploy-action',
 '/tajmone/awesome-interactive-fiction',
 '/stve/awesome-dropwizard',
 '/opensourcecities/montreal']
 

headers = {"Authorization": f"token {github_token}", "User-Agent": github_username}

if headers["Authorization"] == "token " or headers["User-Agent"] == "":
    raise Exception(
        "You need to follow the instructions marked TODO in this script before trying to use it"
    )


def github_api_request(url: str) -> Union[List, Dict]:
    response = requests.get(url, headers=headers)
    response_data = response.json()
    if response.status_code != 200:
        raise Exception(
            f"Error response from github api! status code: {response.status_code}, "
            f"response: {json.dumps(response_data)}"
        )
    return response_data


def get_repo_language(repo: str) -> str:
    url = f"https://api.github.com/repos{repo}"
    repo_info = github_api_request(url)
    if type(repo_info) is dict:
        repo_info = cast(Dict, repo_info)
        return repo_info.get("language", None)
    raise Exception(
        f"Expecting a dictionary response from {url}, instead got {json.dumps(repo_info)}"
    )


def get_repo_contents(repo: str) -> List[Dict[str, str]]:
    url = f"https://api.github.com/repos{repo}/contents/"
    contents = github_api_request(url)
    if type(contents) is list:
        contents = cast(List, contents)
        return contents
    raise Exception(
        f"Expecting a list response from {url}, instead got {json.dumps(contents)}"
    )


def get_readme_download_url(files: List[Dict[str, str]]) -> str:
    """
    Takes in a response from the github api that lists the files in a repo and
    returns the url that can be used to download the repo's README file.
    """
    for file in files:
        if file["name"].lower().startswith("readme"):
            return file["download_url"]
    return ""


def process_repo(repo: str) -> Dict[str, str]:
    """
    Takes a repo name like "gocodeup/codeup-setup-script" and returns a
    dictionary with the language of the repo and the readme contents.
    """
    contents = get_repo_contents(repo)
    readme_contents = requests.get(get_readme_download_url(contents)).text
    return {
        "repo": repo,
        "language": get_repo_language(repo),
        "readme_contents": readme_contents,
    }


def scrape_github_data() -> List[Dict[str, str]]:
    """
    Loop through all of the repos and process them. Returns the processed data.
    """
    return [process_repo(repo) for repo in REPOS]


if __name__ == "__main__":
    data = scrape_github_data()
    json.dump(data, open("data2.json", "w"), indent=1)
    
def get_github_data(cached=False):
    '''
    reads in github data and caches if it hasnt been already. 
    '''
    filename = 'github_readme.csv'
    if cached == False or os.path.isfile(filename) == False:
        df = pd.DataFrame(scrape_github_data())
        df.to_csv(filename)
    else:
        df = pd.read_csv(filename, index_col = 0)

    return df