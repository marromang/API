
% include('header.tpl')
    <div class="docs-content">
      <h3> Tus listas </h3>
      %for lista in listas_usuario['items']:
      	 <li><a href="{{lista["external_urls"]}}" >{{lista["name"]}}</a></li>
          
      %end
	</div>
% include('footer.tpl')
