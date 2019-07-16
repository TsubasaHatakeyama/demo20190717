#####パラメータ設定#####
#リソースグループを指定
$resourceGroupName ='demo-RG<社員番号>'
# Webアプリ名(WebAppsの名前)
$webappname="weathersearch<社員番号>"
# スロット名
$slotname="demo"
#####パラメータ設定#####


# 運用環境のslotへスワップ
Switch-AzWebAppSlot -Name $webappname -ResourceGroupName $resourceGroupName -SourceSlotName $slotname -DestinationSlotName production


