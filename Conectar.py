import psycopg2
import datetime

conn = psycopg2.connect(host="localhost", database="Libreria", user="postgres", password="Admin")

def comprobarCliente(user, password):
    
    cur= conn.cursor()
    comando = "select c.correo, c.contrasena from cliente c where c.correo = '"+user+"' and c.contrasena = '"+password+"'"
    cur.execute(comando)
    rows = cur.fetchall() ##pasar arreglo a la variable row
    conn.commit()

    if (len(rows)==0):
        print("no se encontro")
        return False
    else:
        print("Se encontro")
        return True

#comprobarCliente("ernesto@gmail.com" , "123")        
    


def LibrosMasVendidos():
    cur = conn.cursor()
    comando = "select l.nombre, to_char(l.precio, '$999,999'), l.imagen, l.isbn from libro l join libroxcompra x using (isbn) join boleta b using (boleta_id) group by l.nombre, l.precio, l.imagen, l.isbn order by sum(x.cantidad_comprada) DESC"
    cur.execute(comando)
    rows = cur.fetchall()
    conn.commit()
    return rows

#print(LibrosMasVendidos())
#buscador de lirbros por nombre o isbn

def buscadorNombreIsbn(nombre):
    cur = conn.cursor()
    comando= "select isbn, libro_id, nombre, to_char(fecha_publicacion, 'dd/mm/yyyy'), to_char(precio, '$999,999'),sinopsis, stock_actual, autor, calificacion, imagen, calificaciones from libro join inventario using(isbn) where  nombre = '"+nombre+"'"
    #comando = "select * from libro l where  l.nombre = '"+nombre+"'"
    cur.execute(comando)
    rows = cur.fetchall()
    conn.commit()
    #print(rows)
    return rows

#print(buscadorNombreIsbn('Vagabond 01'))

#retornar cliente para guardarlo en el inicio de sesion para cuando vaya a comprar quede registrado
def traerClienteId(user, password):
    
    cur= conn.cursor()
    comando = "select c.cliente_id from cliente c where c.correo = '"+user+"' and c.contrasena = '"+password+"'"
    cur.execute(comando)
    rows = cur.fetchall() ##pasar arreglo a la variable row
    conn.commit()
    return rows


#crear una compra para esto debemos asegurarnos cuantas compras ya hay para crear el id entonces creamos un metodo
#que nos diga el numero de compras actual

def NumeroComrpras():
    cur = conn.cursor()
    comando = "select count(c.boleta_id) from boleta c"
    cur.execute(comando)
    rows = cur.fetchall()
    conn.commit()
    id= int(rows[0][0]) + 1
    print(id)
    return id

def agregarCompra(id_client, precioLibro):
    cur = conn.cursor()
    id = NumeroComrpras()
    fecha = datetime.datetime.now()
    comando="insert into boleta(boleta_id, fecha, total, cliente_id)                                values("+str(id)+",'"+str(fecha.strftime("%d/%m/%Y"))+"',"+str(precioLibro)+","+str(id_client)+")"
    print("comando= "+comando)
    cur.execute(comando)
    print("creado")
    conn.commit()
    return id

def agregarCompraLibro(isbn, cantidadComrpada, id_client, precioLibro ):
    cur = conn.cursor()
    idComrpa=agregarCompra(id_client, precioLibro)
    comando ="insert into libroxcompra values("+isbn+","+str(idComrpa)+","+cantidadComrpada+")"
    cur.execute(comando)
    print("creado con exito")
    conn.commit()
    
#agregarCompraLibro("9788466657662", "2", "2", "28530")

#retornnamos calificacion y la cantida de gente que a votado para sacar un promedio
def valCant(isbn):
    cur = conn.cursor()
    comando = "select l.calificacion, l.calificaciones from libro l where l.isbn = '"+str(isbn)+"'"
    cur.execute(comando)
    rows = cur.fetchall()
    conn.commit()
    return rows
    

#print(valCant(9788481093353))
#ahora debemos ejecutar la validacion cada vez que se presiona el boton y esto actualizara la BD.
def valorar(isbn, numero):
    cur = conn.cursor()
    rows = valCant(isbn)
    suma=((rows[0][0])*rows[0][1])
    a=((suma)+ numero )
    cantidad=((rows[0][1])+1) 
    promedio = int(a/cantidad)
    
    print(promedio , cantidad)
    comando = "update libro set calificacion ='"+str(promedio)+"', calificaciones= '"+str(cantidad)+"' where isbn = '"+str(isbn)+"'"
    cur.execute(comando)
    conn.commit()
    print("se ha modificado con exito")

#isbn es el id general del libro que vamos a valorar y "numero" es nuestra puntuacion de 1 a 5

#valorar(9788466657662, 5)

#retornar los libros mas valorados
#select l.nombre, l.precio, l.imagen, l.calificacion from libro l  order by calificacion DESC
def librosMasValorados():
    cur = conn.cursor()
    comando="select l.nombre, to_char(l.precio, '$999,999'), l.imagen, l.calificacion from libro l  order by calificacion DESC"
    cur.execute(comando)
    rows = cur.fetchall()
    conn.commit()
    return rows

#print(librosMasValorados())


#retornar los libros mas nuevos pro fecha de la publicacion 
def LibrosMasNuevos():
    cur = conn.cursor()
    comando="select l.nombre, to_char(l.precio, '$999,999'), l.imagen from libro l  order by l.fecha_publicacion DESC"
    cur.execute(comando)
    rows = cur.fetchall()
    conn.commit()
    return rows

#funcion para contar cuantos clientes hay y crear uno nuevo despues
def contarClientes():
    cur = conn.cursor()
    comando="select count(c.cliente_id) from cliente c"
    cur.execute(comando)
    rows = cur.fetchall()
    conn.commit()
    return rows


def agregarCliente( nombre, apellido, fecha_nacimiento, direccion, telefono, correo, contrasena):
    cur = conn.cursor()
    a = contarClientes()
    id = a[0][0] + 1

    comando="insert into cliente values('"+str(id)+"','"+nombre+"','"+apellido+"','"+fecha_nacimiento+"','"+direccion+"','"+telefono+"','"+correo+"','"+contrasena+"')"
    cur.execute(comando)
    print("creado con exito")
    conn.commit()

##SEOKJINTEAMOOOO
#Benja troll
#Que gila porfavor dejemos de llorar por todas las notas existentes pipipipipipi
#se terminan los comentarios en el main
