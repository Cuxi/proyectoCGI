#!/usr/bin/perl

use CGI;
$query = new CGI;
#declaramos la entrada del CGI
print $query->header(-charset=>'utf-8');
print $query->start_html('Respuesta:');

#declaramos el formulario que se va a ver
if (!$query->param) {
	print $query->start_form;
    print $query->textfield(-name=>'categoria',
        -size=>40,
        -maxlength=>40);
    print $query->br;
    print $query->submit(-value=>'Submit tu categoría');
    print $query->end_form;
}


if ($query->param('categoria')){
	$false;
	#recogemos el parámetro categoría del formulario y recorremos el fichero para corroborar que existe la categoria
	$categoria=$query->param('categoria');
	$filename="/tmp/Categorias";
	open F, $filename or die "Imposible abrir: $!";
	$size= -s $filename;
	read(F,$buf,$size);
	close F;
	my @cat=split("\n",$buf);
	
	foreach $cla(@cat) {

		#comparamos el array de categorias con el parámetro recibido
	   if($categoria =~ $cla){
			#recoremos el fichero de productos para imprimir los datos de aquellos que coinciden con la categoría
			$fileproductos="/tmp/TP1";
			open Fi, $fileproductos or die "Imposible abrir: $!";
			$sizes= -s $fileproductos;
			read(Fi,$buff,$sizes);
			close Fi;
			@lineas=split("\n",$buff);
			foreach $l (@lineas) {
				($ca)=split("-",$l);
				if($ca =~ $categoria){
					@campos=split(":",$l);
					#guardamos los datos en un hash
			   		$unhash{$campos[0]}=$campos[1] if($campos[1]);
			   		$false='t';
				}

			   	
			}
			# mostramos el contenido del hash
			foreach $clave(keys %unhash) {
			   print $query->h3($clave, "----->",$unhash{$clave},"\n");
			}
		}else{
			$false='f';
		}



	}
	if($false=='f'){
		#en caso de que no exista no entramos en recorrer el fichero
		print $query->h1('Categoria:',$categoria);
		print $query->h1('No existe');
	}

}

print $query->end_html;
