% include('header.tpl')
<body> 
	<div class="wrapper row3">
    <main class="container clear"> 
      <div class="group btmspace-80">
        <article>
         <h2>Info de {{song}}</h2>
         
         		<h3>Pertenece al album {{album}}</h3>
                <h3>Historia</h3>
                %for i in xrange(0,len(data)):
                 <h1>{{data[0]}}</h1>
                %end
         
        </article>
      </div>
</body>
%include('footer.tpl')