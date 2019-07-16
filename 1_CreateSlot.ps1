#####パラメータ設定#####
#リソースグループを指定
$resourceGroupName ='demo-RG<社員番号>'
# Webアプリ名(WebAppsの名前)
$webappname="weathersearch<社員番号>"
# スロット名
$slotname="staging"
#####パラメータ設定#####


#ステージング環境用スロット「staging」を作成
New-AzWebAppSlot -Name $webappname -ResourceGroupName $resourceGroupName -Slot $slotname

