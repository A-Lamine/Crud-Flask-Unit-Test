<!DOCTYPE html>
<html lang="en">

<head>


    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
        integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <meta charset="UTF-8">
    <title>Manage Movies </title>
</head>

<body>
    <div class="container">
        <div class="row">
            <div class="col md-12">

                <div class="jumbotron p-3">

                    <h2>Manage <b>Movies </b> <button type="button" class="btn btn-success float-right"
                            data-toggle="modal" data-target="#mymodal">Add New Movies</button> </h2>


                    {% with messages = get_flashed_messages() %}

                    {% if messages %}

                    {% for message in messages %}

                    <div class="alert alert-success alert-dismissable" role="alert">

                        <button type="button" class="close" data-dismiss="alert" aria-label="close">

                            <span aria-hidden="true">x</span>

                        </button>


                        {{message}}


                    </div>


                    {% endfor %}

                    {% endif %}
                    {% endwith %}


                    <table id="example" class="table table-striped table-bordered" style="width:100%">

                        <tr>

                            <th>ID</th>
                            <th>Url</th>
                            <th>Title</th>
                            <th>Action</th>


                        </tr>


                        {% for row in movies %}
                        <tr>
                            <td>{{row.id}}</td>
                            <td>{{row.url}}</td>
                            <td>{{row.title}}</td>


                            <td>
                                <a href="/update/{{row.id}}" class="btn btn-warning btn-xs" data-toggle="modal"
                                    data-target="#modaledit{{row.id}}">Edit</a>
                                <a href="/delete/{{row.id}}" class="btn btn-danger btn-xs"
                                    onclick="confirm('Are You Sure To Delete ?')">Delete</a>


                            </td>

                        </tr>


                        <!-- Modal Edit movie-->
                        <div id="modaledit{{row.id}}" class="modal fade" role="dialog">
                            <div class="modal-dialog">


                                <div class="modal-content">


                                    <div class="modal-header">


                                        <h4 class="modal-title">Update Information</h4>


                                    </div>


                                    <div class="modal-body">


                                        <form action="{{url_for('main.update')}}" method="POST">


                                            <div class="form-group">


                                                <label>Url:</label>
                                                <input type="hidden" name="id" value="{{row.id}}">

                                                <input type="text" class="form-control" name="url" value="{{row.url}}">

                                            </div>
                                            <div class="form-group">


                                                <label>Title:</label>

                                                <input type="text" class="form-control" name="title"
                                                    value="{{row.title}}">

                                            </div>

                                            <div class="form-group">


                                                <button class="btn btn-primary" type="submit">Update</button>


                                            </div>


                                        </form>


                                    </div>


                                    <div class="modal-footer">


                                        <button type="button" class="btn btn-secondary"
                                            data-dismiss="modal">Close</button>


                                    </div>


                                </div>


                            </div>

                        </div>


                        {% endfor %}


                    </table>


                </div>



                <!-- Modal Add movie-->


                <div id="mymodal" class="modal fade" role="dialog">
                    <div class="modal-dialog">
                        <div class="modal-content">
                            <div class="modal-header">

                                <h4 class="modal-title">Add movie</h4>
                            </div>
                            <div class="modal-body">

                                <form action="{{url_for('main.insert')}}" method="POST">


                                    <div class="form-group">

                                        <label>Url:</label>
                                        <input type="text" class="form-control" name="url" required="1">


                                    </div>
                                    <div class="form-group">

                                        <label>Title:</label>
                                        <input type="text" class="form-control" name="title" required="1">


                                    </div>

                                    <div class="form-group">


                                        <button class="btn btn-primary" type="submit">Add movie</button>


                                    </div>


                                </form>


                            </div>


                            <div class="modal-footer">


                                <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>


                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js"
        integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n"
        crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js"
        integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo"
        crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js"
        integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6"
        crossorigin="anonymous"></script>
</body>