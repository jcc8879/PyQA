jQuery(document).ready(function($) {
	var originalNote = '';

	$(".notecell").bind('click', function(){
		//hide the text, and show a textarea so they can edit
		$(this).children(".latestnote").hide();
		$(this).children(".hiddennote").show();
		$(this).children(".hiddennote").focus();

		//set a "global" variable so we can see if they actually update the note
		originalNote = $(this).children(".hiddennote").val();

	});

	$(".hiddennote").bind('blur', function(){
		var newNote = $(this).val();

		if(newNote != originalNote){
			//they changed the note, so add a new one into the db
			
		}

		$(this).parent("td").children(".latestnote").text(newNote);
		$(".latestnote").show();
		$(".hiddennote").hide();

		originalNote = '';
	});
});