$(document).ready(function () {
    $('.js-example-basic-multiple').select2();
});

// $(document).ready(function() {
//     $('#mission_list').DataTable( {
//         select: {
//             style: 'multi'
//         }
//     } );
// } );

$(document).ready(function () {
    $('#shuttle_table').DataTable({
        columnDefs: [{
            orderable: false,
            className: 'select-checkbox',
            targets: 0
        }],
        select: {
            style: 'os',
            selector: 'td:first-child'
        },
        order: [[1, 'asc']]
    });
});

$(document).ready(function () {
    // var DT1 = $('#mission_list').DataTable( {
    //     columnDefs: [ {
    //         orderable: false,
    //         className: 'select-checkbox',
    //         targets:   0
    //     } ],
    //     select: {
    //         style:    'multi',
    //         selector: 'td:first-child'
    //     },
    //     order: [[ 1, 'asc' ]]
    // } );

    var DT1 = $('#mission_list').DataTable({
        select: {
            style: 'multi'
        }
    });
    $(".selectAll").on("click", function (e) {
        if ($(this).is(":checked")) {
            DT1.rows().select();
        } else {
            DT1.rows().deselect();
        }
    });
});

$(document).ready(function () {
    $('#candidate_list').DataTable({
        select: {
            style: 'multi'
        }
    });
});


