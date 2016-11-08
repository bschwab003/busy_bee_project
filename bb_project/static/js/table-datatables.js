

// INIT DATATABLES
$(function () {
	// Init
    var spinner = $( ".spinner" ).spinner();
    var table = $('#table_id').dataTable( {
        "lengthMenu": [[25, 50, 100, -1], [25, 50, 100, "All"]]
    } );

    var tableTools = new $.fn.dataTable.TableTools( table, {
    	"sSwfPath": "static/vendors/DataTables/extensions/TableTools/swf/copy_csv_xls_pdf.swf",
        "buttons": [
            "copy",
            "csv",
            "xls",
            "pdf",
            { "type": "print", "buttonText": "Print me!" }
        ]
    } );
    $(".DTTT_container").css("float","right");
});


