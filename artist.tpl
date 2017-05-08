% include('header.tpl')
<body> 
	<div class="wrapper row3">
    <main class="container clear"> 
      <div class="group btmspace-80">
        <article>
         <h3>Biografía de {{artist}}.</h3>
         %for b in {{bio}}:
                 <h1>b</h1>
                %end

        </article>
      </div>
</body>
%include('footer.tpl')
