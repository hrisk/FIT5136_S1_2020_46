print("Content-Type： text/html")
print()
print("""
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-datetimepicker/4.17.43/css/bootstrap-datetimepicker.min.css">
    <link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-datetimepicker/4.17.43/css/bootstrap-datetimepicker-standalone.css">
    <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-datetimepicker/4.17.43/js/bootstrap-datetimepicker.min.js"></script>
    <title>Feature 1</title>
  </head>

  <body>
    <h1 align="center">Mission Table</h1>
    <button type="button" class="btn btn-outline-secondary float-right">Logout</button>

    <table class="table table-borderless">
        <tbody>
            <tr>
                <td>Name</td>
                <td>
                    <input type="text" class="form-control" id="input1" placeholder="Enter Name">
                </td>
                <td>Country</td>
                <td>
                    <input type="text" class="form-control" id="input2" placeholder="Input Country">
                </td>
                <td>Status</td>
                <td>
                    <select class="form-control" id="exampleFormControlSelect1">
                        <option>a.Planning phase</option>
                        <option>b.Departed Earth</option>
                        <option>c.Landed on Mars</option>
                        <option>d.Mission in Progress</option>
                        <option>e.Returned to Earth</option>
                        <option>f.Mission Completed</option>
                    </select>
                </td>
            </tr>
            <tr>
             <td>Launch Date</td>
             <td>
                    <div class="container">
                        <div class="row">
                            <div class='col-sm-6'>
                                <div class="form-group">
                                    <div class='input-group date' id='datetimepicker1'>
                                        <input type='text' class="form-control" />
                                        <span class="input-group-addon">
                                            <span class="glyphicon glyphicon-calendar"></span>
                                        </span>
                                    </div>
                                </div>
                            </div>
                            <script type="text/javascript">
                                $(function () {
                                    $('#datetimepicker1').datetimepicker({
                                    format : 'dd/mm/yyyy'});
                                });
                            </script>
                        </div>
                    </div>

              </td>

              <td>Location</td>
              <td>
                  <input type="text" class="form-control" id="input3" placeholder="Location">
              </td>
              <td>Duration</td>
              <td>
                  <input type="number" class="form-control" id="input4" placeholder="Duration">
              </td>
            </tr>
       </tbody>

    </table>
    <div class="form-group row float-right">
        <div class="col-md-4">
               <button type="button" class="btn btn-secondary btn-sm">Reset</button>
        </div>
        <div class="col-md-4">
               <button type="button" class="btn btn-primary btn-s">Search</button>
        </div>
        </div>

    <div class="form-group row float-left">
        <div class="col-md-4">
                <button type="button" class="btn btn-primary btn-sm">Add</button>
        </div>
        <div class="col-md-4">
                <button type="button" class="btn btn-primary btn-sm">Delete</button>

            </div>
    </div>

    <!-- Table  -->
    <table class="table table-bordered">
      <!-- Table head -->
      <thead>
        <tr>
          <th>
            <!-- Default unchecked -->
            <div class="custom-control custom-checkbox">
              <input type="checkbox" class="custom-control-input" id="tableDefaultCheck1">
              <label class="custom-control-label" for="tableDefaultCheck1"></label>
            </div>
          </th>
          <th>Name</th>
          <th>Description</th>
          <th>Country of Origin</th>
          <th>Countries allowed</th>
          <th>Coordinator name&Contact</th>
          <th>Job desc</th>
          <th>Cargo Req</th>
          <th>Launch Date</th>
          <th>Location</th>
          <th>Duration</th>
          <th>Status</th>
          <th>Operations</th>
        </tr>
      </thead>
      <!-- Table head -->

      <!-- Table body -->
      <tbody>
        <tr>
          <th scope="row">
            <!-- Default unchecked -->
            <div class="custom-control custom-checkbox">
              <input type="checkbox" class="custom-control-input" id="tableDefaultCheck2" checked>
              <label class="custom-control-label" for="tableDefaultCheck2"></label>
              <td>Mark</td>
              <td>Go to mars and find oxygen</td>
              <td>Australia</td>
              <td>China, India, Japan</td>
              <td>Joey +61411123123</td>
              <td>find oxygen</td>
              <td>
              <button type="button" class="btn btn-outline-primary">View</button>
              </td>
              <td>03/06/2020</td>
              <td>123 Clayton Rd, VIC,AU</td>
              <td>30</td>
              <td>Planning phase</td>
              <td>
              <button type="button" class="btn btn-outline-primary">Edit</button>
              <button type="button" class="btn btn-outline-primary">Select shuttle</button>
              <button type="button" class="btn btn-outline-primary">Select candidates</button>
              </td>
            </div>
          </th>

        </tr>
        <tr>
          <th scope="row">
            <!-- Default unchecked -->
            <div class="custom-control custom-checkbox">
              <input type="checkbox" class="custom-control-input" id="tableDefaultCheck3">
              <label class="custom-control-label" for="tableDefaultCheck3"></label>
            </div>
          </th>

        </tr>
        <tr>
          <th scope="row">
            <!-- Default unchecked -->
            <div class="custom-control custom-checkbox">
              <input type="checkbox" class="custom-control-input" id="tableDefaultCheck4">
              <label class="custom-control-label" for="tableDefaultCheck4"></label>
            </div>
          </th>

        </tr>
      </tbody>
      <!-- Table body -->
    </table>
    <!-- Table  -->










  </body>
  </html>
""")