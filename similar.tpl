% include('header.tpl')
<body> 
	<div class="wrapper row3">
    <main class="container clear"> 
      <div class="group btmspace-80">
        <article>
         <h1>Similar to {{artist}}</h1>
         <ul>
         		%for s,u in zip(similar, urls):
                    <li><a href="{{u}}">{{s}}</a></li>
                %end
         </ul>
        </article>
      </div>
</body>
%include('footer.tpl')
