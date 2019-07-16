#####パラメータ設定#####
# GitHubのリポジトリ
$githubrepo="https://github.com/tomokofuse/WeatherSearch.git"
# リモートリポジトリ
$rmrepo="azure<社員番号>"
# GitクローンURL
$giturl="https://dp<社員番号>@weathersearch<社員番号>-staging.scm.azurewebsites.net:443/weathersearch<社員番号>.git"
#####パラメータ設定#####


# GitHubからソースを取得
git clone $githubrepo 
cd WeatherSearch

#Azure用の空のリモートリポジトリ作成
git remote add $rmrepo $giturl

#Azure用のリモートリポジトリにお天気アプリのソースをデプロイ（プッシュ）
git push $rmrepo master


