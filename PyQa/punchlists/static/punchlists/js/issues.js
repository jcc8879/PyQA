jQuery(document).ready(function($) {
	var originalNote = '';

	$(".latestnote").bind('click', function(){
		//hide the text, and show a textarea so they can edit
		$(this).parent('div').children("span.latestnote").hide();
		$(this).parent('div').children("form").children(".hiddennote").show();
		$(this).parent('div').children("form").children(".hiddennote").focus();

		//set a "global" variable so we can see if they actually update the note
		originalNote = $(this).parent('div').children("form").children(".hiddennote").val();

	});

	$(".hiddennote").bind('blur', function(){
		var issue_id = $(this).parent('form').children(".issue_id").val();
		var newNote  = $(this).val();
		var noteForm = $(this).parent('form');

		if(newNote != originalNote){
			//they changed the note, so add a new one into the db
			var postData = $.post( "issue/addnote/"+issue_id+"/", noteForm.serialize(), function(data) {
									console.log(data);
								})
								.fail(function(data){
									console.log(data);
								});
		}
		
		$(this).parent('form').parent("div").children("span.latestnote").text(newNote);
		$(".latestnote").show();
		$(".hiddennote").hide();

		originalNote = '';
	});
});