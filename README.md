#¿Qué es??
La forma en que un programa abre, lee, escribe, modifica y cierra archivos que están guardados en la computadora.
Manejo de archivos = que tu programa pueda hablar con los archivos de tu compu (abrirlos, leerlos y escribirlos).

#¿Para qué sirve?
  - Guardar información para usarla más tarde (por ejemplo: resultados, notas, datos).
  - Leer datos que ya están guardados sin tener que escribirlos en el código.
  - Crear reportes, logs, etc.

#  Sintaxis =>
      open("archivo",modo,encoding=None):
# modo => 
      r= read (modo de lectura), 
      w=write(abre para escritura y borra todo lo anterior),
      a=append (agregar al final sin borrar), 
      b= binary (modo binario para agregar images)
# metodos para leer => 
      .read(lee todo como un solo string),
      .readline(lee una linea por ves),  
      .readlines(lee todo y lo devuelve como una lista)
# metodos para escribir => 
      .write("escribe un solo string"), 
      .writelines(["texto1","texto2"]) (escribe una lista de strings, varias cadenas de texto)
# metodos para cerrar => 
      .close() (cierra el archivo)
      ... 
      with open("archivo", modo, encoding=) as f: (cierra el archivo automaticamente al terminar el bloque de codigo) 
      f.code(para chequear si se cerro el archivo)
