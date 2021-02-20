$(document).ready(function(){
    $("#id_name").addClass('form-control');
  
  
  
  $('#task_form').submit(function(e){
      e.preventDefault();
      var serialData = $(this).serialize();
      
      
      $.ajax({
          type: 'POST',
          url: '{% url "add_task_ajax" list.id %}',
          data: serialData,
          success: function (response) {
            $('#task_form').trigger('reset');
            var instance = JSON.parse(response['instance']);
            
            var fields  = instance[0]['fields'];
            var pk = instance[0]['pk'];
            
              $('.list-group').prepend(`
              
              
                    <span class="list-group-item" id='task${pk}'>
                  <li>
                    <a>${fields['name']}</a>
                  </li> 
                  <button class="btn btn-primary">
                    <a href="#" style='color: white;' id="${pk}">Done</a>
                  </button>
                </span>
              
              `);
  
  
  
          },
  
          error: function(response){
  
            alert(response["responseJSON"].error);
  
          }
        });
      
  
  
  });
  
  $(".list-group").on("click",'span a',function(event){
      event.preventDefault();
      var id = $(event.target).attr('id');
      var element_id = 'task'+id;
      var elem = document.querySelector(`#task${id}`);
      
  
      $.ajax({
        type: "GET",
        url: "{% url 'done_task_ajax' %}",
        data: {"task_id": id},
  
        success: function(response){
            if(response['delete']){
                
                console.log("success");
                elem.parentNode.removeChild(elem);
            }
        },
        error: function(response){
            console.log(response);
        }
      })
    
  });
  
  
  
  
  
  
  
  });  
  