
% include('header.tpl')
    <div class="docs-content">
      <h3> Tus listas </h3>
      %for lista in listas_usuario['items']:
          <li>{{lista["tracks"]["href"]}}{{lista["name"]}}</li>	 
      %end
	</div>
% include('footer.tpl')
