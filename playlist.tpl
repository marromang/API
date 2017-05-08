
% include('header.tpl')
    <div class="wrapper row3">
    <main class="container clear"> 
      <div class="group btmspace-80">
        <article>
      		<h3> Tus listas </h3>
      		%for lista in listas_usuario['items']:
      	 		<li><a href="{{lista["external_urls"]["spotify"]}}" >{{lista["name"]}}</a></li>
      		 %end
	</article>
	</div>
     </main>
     </div>
% include('footer.tpl')
