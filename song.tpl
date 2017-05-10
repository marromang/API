% include('header.tpl')
<body> 
	<div class="wrapper row3">
    <main class="container clear"> 
      <div class="group btmspace-80">
        <article>
         <h2>{{song}} info</h2>
         
         		<h3>Belongs to  {{album}}</h3>
                <h3>Wiki</h3>
                 <p>{{data[0]}}</p>
                %end
         
        </article>
      </div>
</body>
%include('footer.tpl')
