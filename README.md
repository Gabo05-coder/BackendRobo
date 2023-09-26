This is a project made to manage posts as an REST API using Django Rest Framework.
aagregamos weas


Este código es una configuración de base de datos en Python, específicamente para un proyecto de Django que usa una base de datos MySQL. La configuración se lleva a cabo a través de un diccionario llamado DATABASES, que contiene una clave llamada "default" que contiene un conjunto de opciones de configuración de base de datos.
DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': os.environ.get('DB_NAME'),
    'HOST': os.environ.get('DB_HOST'),
    'PORT': os.environ.get('DB_PORT'),
    'USER': os.environ.get('DB_USER'),
    'PASSWORD': os.environ.get('DB_PASSWORD'),
    'OPTIONS': {'ssl': {'ca': os.environ.get('MYSQL_ATTR_SSL_CA')}}
  }
}
Este código establece la conexión de la base de datos para un proyecto Django y utiliza variables de entorno para almacenar datos privados como el nombre de usuario, la contraseña y los detalles de conexión. Se le puede conocer como una práctica común para proteger esta información confidencial y permitir una configuración más adaptable en diferentes entornos de despliegue.

Aquí está lo que hace cada parte del código:
'ENGINE': 'django.db.backends.mysql': Esto crea el motor de base de datos que utilizará Django para trabajar con MySQL. 
'NAME': os.environ.get('DB_NAME'): El nombre de la base de datos se obtiene de la variable de entorno 'DB_NAME'. Es crucial que el nombre de la base de datos indique a qué base de datos se conectará el proyecto Django.
'HOST': os.environ.get('DB_HOST'): Esto utiliza la variable de entorno 'DB_HOST' para obtener la dirección del host de la base de datos. El servidor de la base de datos al que Django se conectará se conoce como host.
'PORT': os.environ.get('DB_PORT'): Esto obtiene el número de puerto de conexión de la base de datos de la variable de entorno denominada "DB_PORT". Este puerto es necesario para conectarse a un servidor de base de datos en un host determinado.
'USER': os.environ.get('DB_USER'): Esto obtiene el nombre de usuario para la autenticación en la base de datos desde una variable de entorno llamada 'DB_USER'.
'PASSWORD': os.environ.get('DB_PASSWORD'): Esto obtiene la contraseña del usuario de la base de datos desde una variable de entorno.
'OPTIONS': {'ssl': {'ca': os.environ.get('MYSQL_ATTR_SSL_CA')}}: Esto proporciona opciones adicionales de configuración. En este caso, está configurando la opción de SSL para la conexión a la base de datos y obtiene el archivo de certificado desde una variable de entorno llamada 'MYSQL_ATTR_SSL_CA'


2
 Usando estas variables, la aplicación puede conectarse a la base de datos utilizando el nombre de usuario, la contraseña, la dirección del servidor y el puerto especificados, y también puede establecer una conexión segura utilizando el certificado SSL 

DB_NAME=jicproyect
DB_USER=4blmby9pbh6x6w35lfc9
DB_PASSWORD=pscale_pw_ovJuchQAGX14kbOfzG7YBzrK3bjbhk1A1aFludr7qN4
DB_HOST=aws.connect.psdb.cloud
DB_PORT=3306
MYSQL_ATTR_SSL_CA=/etc/ssl/certs/ca-certificates.crt

DB_NAME: Esta variable almacena el nombre de la base de datos, que en este caso se llama "jicproyect".

DB_USER: Almacena el nombre de usuario que se utilizará para autenticarse en la base de datos. El valor es "4blmby9pbh6x6w35lfc9".

DB_PASSWORD: Almacena la contraseña correspondiente al usuario de la base de datos. El valor parece ser una cadena de caracteres larga y compleja que proporciona seguridad para la autenticación. En este caso, la contraseña es "pscale_pw_ovJuchQAGX14kbOfzG7YBzrK3bjbhk1A1aFludr7qN4".

DB_HOST: Esta variable almacena la dirección del servidor de la base de datos al que se debe conectar la aplicación. El valor es "aws.connect.psdb.cloud".

DB_PORT: Almacena el número de puerto al que se debe conectar la aplicación para interactuar con la base de datos. En este caso, el puerto es 3306, que es el puerto estándar utilizado por MySQL. (al parecer)

MYSQL_ATTR_SSL_CA: Esta variable almacena la ubicación del archivo de certificado SSL que se utilizará para establecer una conexión segura a la base de datos. El valor es "/etc/ssl/certs/ca-certificates.crt", lo que indica la ubicación del archivo de certificado en el sistema.

clonado python manage.py runserver ttp://127.0.0.1:8000/api/dataAC

25/9/23 carpeta de migracion es la convercion de los codgios a lenguaje sql en migracion de forma alter table siver para que el sistema funciones en diferentes computadores, como una forma automaticamente los archivos para evitar errores. creacion de un nueva funcion para mostrar la opciones creadas dentro de los modelos creando un formulario de datos Forms.py class DataViewSet(viewsets.ModelViewSet): queryset = dataAC.objects.all() serializer_class = DataSerializer cracion de una clase para vista de los datos en DataAC MODE_CHOICES = ( ('Auto', 'Auto'), ('Manual', 'Manual'), )

STATUS_CHOICES = (
    ('On', 'On'),
    ('Off', 'Off'),
) //seccion en models para las opciones de encendido y apagado de la AC

 la clase models.Model. Esta clase representa un modelo de datos en Django
 MODE_CHOICES: Es una tupla que define las opciones para el campo mode. El campo mode es una cadena de texto que puede tener los valores 'Auto' o 'Manual'.

STATUS_CHOICES: Es una tupla que define las opciones para el campo status. El campo status es una cadena de texto que puede tener los valores 'On' o 'Off'.

name, mark, model, location, conectionCode: Estos son campos de texto que almacenan información relacionada con el nombre, marca, modelo, ubicación y código de conexión respectivamente.

mode: Es un campo de texto que almacena el modo de funcionamiento del dispositivo. Puede tener los valores 'Auto' o 'Manual' según la elección del usuario.
status: Es un campo de texto que almacena el estado del dispositivo. Puede tener los valores 'On' o 'Off' según la elección del usuario.
 representa un modelo de datos que se puede utilizar para almacenar y manipular información relacionada con dispositivos de aire acondicionado en una base de datos utilizando Django.

 la clase forms.Form. Esta clase representa un formulario en Django
 opciones: Es un campo de selección que permite al usuario elegir entre dos opciones: 'Auto' o 'Manual'.
 representa un formulario que se puede utilizar para recopilar información del usuario en una aplicación web Django. Cada instancia de esta clase representa un formulario con un campo de selección llamado opciones.
revisar el archivo 0003_dataac, forms.
