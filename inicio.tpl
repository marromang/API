% include('header.tpl')

<div class="wrapper row3">
<main class="container clear"> 
	<article>
		<h1>BIENVENIDO A MUSIC INFORMATOR.</h1>
		<form action="artist" method="post"> 
			Artista a buscar: <input name="artist" type="text">
				<input value="Buscar artista" type="submit">
		</form>
		<br/>
		<form action="similar" method="post"> 
			Artistas similares a...: <input name="similar" type="text">
			<input value="Buscar artista" type="submit">
		</form>
		<br/>
		<form action="album" method="post"> 
			Album a buscar: <input name="album" type="text">
				<input value="Buscar album" type="submit">
		</form>
		<br/>
		<form action="artistCountry" method="post"> 
			Mejores artistas por país: <input name="artistCountry" type="text">
				<input value="Buscar pais" type="submit">
		</form>
		<br/>
		<form action="songsCountry" method="post"> 
			Mejores canciones por país: <input name="songsCountry" type="text">
				<input value="Buscar pais" type="submit">
		</form>
	</article>
	
</div>
%include('footer.tpl')
