document.addEventListener("deviceready", function () {

    var pictureSource;   // picture source
    var destinationType; // sets the format of returned value

    // pictureSource=navigator.camera.PictureSourceType;
    // destinationType=navigator.camera.DestinationType;


    //--- Namespaced ---//
    var $ReportView = window.$ReportView || {};

    var $App = window.$App || {};

    $App.globals = $App.globals || {};

    $App.globals.baseUrl = 'http://j5gm.t.proxylocal.com';


    $ReportView.formPanel = {
        title: (function () {
            var elem = $('#title');
            return elem;
        }()),
        description: (function () {
            var elem = $('#description');
            return elem;
        }()),
        difficulty: (function () {
            var elem = $('#difficulty');
            return elem;
        }()),
        submit: (function () {
            var elem = $('#submit');
            return elem;
        }())
    };

    $ReportView.formData = {
        imageData: '',
        title: '',
        description: '',
        time: '',
        location: '',
        difficulty: ''
    };


    // Wait for device API libraries to load
    //
    // document.addEventListener("deviceready",onDeviceReady,false);

    // function onDeviceReady() {
    // }

    function onPhotoDataSuccess(imageData) {
        var smallImage = document.getElementById('smallImage');
        smallImage.style.display = 'block';
        smallImage.src = "data:image/jpeg;base64," + imageData;
        $ReportView.formData.imageData = imageData;
    }

    function capturePhoto() {
        // Take picture using device camera and retrieve image as base64-encoded string
        navigator.camera.getPicture(onPhotoDataSuccess, onFail, {
            quality: 50,
            destinationType: Camera.DestinationType.DATA_URL
        });
    }

    function onFail(message) {
        alert('Failed because: ' + message);
    }

    function submit() {

        $ReportView.formData.title = $ReportView.formPanel.title.val();
        $ReportView.formData.description = $ReportView.formPanel.description.val();
        $ReportView.formData.time = new Date().getTime();
        $ReportView.formData.difficulty = $ReportView.formPanel.difficulty.val();

        var onSuccess = function(position) {

            $ReportView.formData.location = {
                lat: position.coords.latitude,
                long: position.coords.longitude
            };

            $.ajax({
                url: $App.globals.baseUrl + '/report',
                type: 'POST',
                data: JSON.stringify($ReportView.formData),
                success: function (reportResponse) {
                    console.log(reportResponse);
                    alert('Sucess');
                    // alert('Success');
                    // alert(JSON.stringify(reportResponse));
                },
                error: function (errorResponse) {
                    alert('Error');
                    alert((JSON.stringify(errorResponse)));
                }
            });

        };
        function onError(error) {
            alert('code: '    + error.code    + '\n' +
                  'message: ' + error.message + '\n');
        }

        navigator.geolocation.getCurrentPosition(onSuccess, onError);

    }


    document.getElementById('submit').addEventListener('click', submit);
    document.getElementById('captureImage').addEventListener('click', capturePhoto);
    document.getElementById('showMap').addEventListener('click', function (evt) {
        $('#viewContainer').html($('#mapView').html());

        
        // drawMap();
    });

});
