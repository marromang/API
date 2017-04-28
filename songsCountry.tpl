% include('header.tpl')
<body> 
	<div class="wrapper row3">
    <main class="container clear"> 
      <div class="group btmspace-80">
        <article>
         <h1>Top 10 songs in {{country}}.</h1>
         <ol>
         		%for a,t in zip(art, tracks):
         			<li>{{a}} - {{t}}</li>
         		%end
         </ol>
        </article>
      </div>
</body>
%include('footer.tpl')