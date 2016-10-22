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

	#recogemos el parámetro categoría del formulario y recorremos el fichero para corroborar que existe la categoria
	$categoria=$query->param('categoria');
	$filename="Categorias";
	open F, $filename or die "Imposible abrir: $!";
	$size= -s $filename;
	read(F,$buf,$size);
	close F;
	my @cat=split("\n",$buf);
	#metemos las categorías en un array
	foreach my $n (@cat){
		push @cat, $n;	
	}
	foreach $cla(keys %cat) {
		#comparamos el array de categorias con el parámetro recibido
	   if($categoria =~ $cla){
			print $query->h1('Categoria:',$categoria);
			print $query->h1('Existe');
			#recoremos el fichero de productos para imprimir los datos de aquellos que coinciden con la categoría
			$filenamedos="TP1";
			open F, $filenamedos or die "Imposible abrir: $!";
			$size= -s $filenamedos;
			read(F,$buf,$size);
			close F;
			@lineas=split("\n",$buf);
			foreach $l (@lineas) {
				$ca=split("-",$l);
				if($ca =~ $categoria){
					@campos=split(":",$l);
					#guardamos los datos en un hash
			   		$unhash{$campos[0]}=$campos[1] if($campos[1]);
				}
			   	
			}
			# mostramos el contenido del hash
			foreach $clave(keys %unhash) {
			   print $clave, "----->",$unhash{$clave},"\n";
			}
		}else{
			#en caso de que no exista no entramos en recorrer el fichero
			print $query->h1('Categoria:',$categoria);
			print $query->h1('No existe');
		}
	}


}

print $query->end_html;