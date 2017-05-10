
% include('header.tpl')
    <div class="wrapper row3">
    <main class="container clear"> 
      <div class="group btmspace-80">
        <article>
      		<h3> Your playlists </h3>
		<ol>
      		%for lista in listas_usuario['items']:
      	 		<li><a href="{{lista["external_urls"]["spotify"]}}" >{{lista["name"]}}</a></li>
      		 %end
		 </ol>
	</article>
	</div>
     </main>
     </div>
% include('footer.tpl')
