% include('header.tpl')
<body> 
	<div class="wrapper row3">
    <main class="container clear"> 
      <div class="group btmspace-80">
        <article>
         <h3>Biografía de {{artist}}.</h3>
         %for i in xrange(0,len(bio)):
                 <h1>{{bio[0]}}</h1>
                %end

        </article>
      </div>
</body>
%include('footer.tpl')
