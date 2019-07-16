#####パラメータ設定#####
#リソースグループを指定
$resourceGroupName ='demo-RG999'
#VM名を指定
$vmname='demo-VM999'
#VMの仮想ネットワークを指定
$vnetname = 'demo-Vnet999'
#複製するVMのサイズを指定
$vmsize = 'Standard_D3_v2'
#リージョンを指定 西日本は「Japan West」
$location = 'Japan East'
#####パラメータ設定#####

# Define user name and blank password
$securePassword = ConvertTo-SecureString ' ' -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential ("azuser", $securePassword)

# Create a resource group
New-AzResourceGroup -Name $resourceGroupName -Location $location

# Create a subnet configuration
$subnetConfig = New-AzVirtualNetworkSubnetConfig -Name "default" -AddressPrefix "192.168.1.0/24"

# Create a virtual network
$vnet = New-AzVirtualNetwork -ResourceGroupName $resourceGroupName -Location $location `
  -Name $vnetname -AddressPrefix "192.168.0.0/16" -Subnet $subnetConfig

# Create a public IP address and specify a DNS name
$pip = New-AzPublicIpAddress -ResourceGroupName $resourceGroupName -Location $location `
  -Name "mypublicdns$(Get-Random)" -AllocationMethod Static -IdleTimeoutInMinutes 4

$nic = New-AzNetworkInterface -Name myNic -ResourceGroupName $resourceGroupName -Location $location `
  -SubnetId $vnet.Subnets[0].Id -PublicIpAddressId $pip.Id

# Create a virtual machine configuration
$vmConfig = New-AzVMConfig -VMName $vmName -VMSize $vmsize |
Set-AzVMOperatingSystem -Linux -ComputerName $vmName -Credential $cred -DisablePasswordAuthentication |
Set-AzVMSourceImage -PublisherName "OpenLogic" -Offer "CentOS" -Skus "7.5" -Version "latest" |
Set-AzVMBootDiagnostic -VM $vmName -Disable |
Add-AzVMNetworkInterface -Id $nic.Id

# Configure SSH Keys
$sshPublicKey = Get-Content ".ssh\id_rsa.pub"
Add-AzVMSshPublicKey -VM $vmconfig -KeyData $sshPublicKey -Path "/home/azuser/.ssh/authorized_keys"

# Create a virtual machine
New-AzVM -ResourceGroupName $resourceGroupName -Location $location -VM $vmConfig
