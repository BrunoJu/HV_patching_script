#coding=utf-8

from selenium import webdriver
import time

profile_directory = r'C:\Users\c5258641\AppData\Roaming\Mozilla\Firefox\Profiles\7870jpat.default'
profile = webdriver.FirefoxProfile(profile_directory)
driver = webdriver.Firefox(profile)
driver.get("https://gmp.wdf.sap.corp/")
time.sleep(8)
driver.get("https://gmp.wdf.sap.corp/cgi-bin/off_dispatch.pl/plan/user")

createTicket_js = r'''var s_blade = prompt("input Source Server: ")
var t_blade = prompt("input Target server: ")
s_blade = s_blade.replace(/\s/ig,'');
t_blade = t_blade.replace(/\s/ig,'');
var ticket = document.getElementsByClassName("btn btn-primary fancybox");
var createdEvent = document.createEvent("MouseEvents");
createdEvent.initMouseEvent("click", true, true);
ticket[0].dispatchEvent(createdEvent)
setTimeout(function(){
var internalWindow = document.getElementsByTagName("iframe")[0].contentWindow
var internalDocument = internalWindow.document
var edit = internalDocument.getElementsByClassName('editcontrol')
edit[3].children[0].innerText = "Hypervisor patching\n\nServer to patch:"+s_blade+"\nDestination Server:"+t_blade+"\n\nPlease follow the documentation:\nhttps://gmp-twiki.wdf.sap.corp/cgi-bin/twiki/bin/view/A1s/A1S_new/ServiceRequest/CrossProductsServices/HypervisorPatching"
edit[3].children[0].value = "Hypervisor patching\n\nServer to patch:"+s_blade+"\nDestination Server:"+t_blade+"\n\nPlease follow the documentation:\nhttps://gmp-twiki.wdf.sap.corp/cgi-bin/twiki/bin/view/A1s/A1S_new/ServiceRequest/CrossProductsServices/HypervisorPatching"
edit[1].children[0].value="M"
var internalDocument = document.getElementsByTagName("iframe")[0].contentWindow.document
var btn_search = internalDocument.getElementsByClassName("ui-button-text")
btn_search[3].dispatchEvent(createdEvent)
btn_search[5].dispatchEvent(createdEvent)
btn_search[3].dispatchEvent(createdEvent)
btn_search[9].dispatchEvent(createdEvent)
btn_search[5].dispatchEvent(createdEvent)
var inventory = internalDocument.getElementsByClassName('glyphicon glyphicon-equalizer')
inventory[1].dispatchEvent(createdEvent)
setTimeout(function(){
internalWindow.$('#inv_search_input').val(s_blade)
internalWindow.inventory_search()
setTimeout(function(){
var table = internalDocument.getElementsByClassName("display table table-striped table-bordered table-hover table-condensed dataTable")
var input_SName = table[0].getElementsByTagName("input")[1]
input_SName.checked=true
internalWindow.inventory_select()
setTimeout(function(){
internalWindow.suggest_field_for_inventory("area")
internalWindow.suggest_field_for_inventory("landscape")
internalWindow.suggest_field_for_inventory("usage_area")
setTimeout(function(){
//internalWindow.save_base()
},2000)
},3000)
},12000)
},8000)
},5000)'''
continue_run = True
while(continue_run):
	time.sleep(5)
	driver.execute_script(createTicket_js)
	result = input("Do you want to run the script again?: (Y/N) ")
	if result == "Y":
		continue_run = True
	else:
		continue_run = False

print("Thanks")
