setInterval(get_data_robot_gripper, 1000)
setInterval(get_data_robot_vacuum, 1000)

function get_data_robot_gripper() {
    $.ajax({
        type: 'GET',
        url: '/robot_gripper_connect',
        dataType: 'json',
        contentType: 'application/json',
        data: {},
        success: function (response) {
            document.getElementById("t1_1").value = response["t1"]
            document.getElementById("t2_1").value = response["t2"]
            document.getElementById("t3_1").value = response["t3"]
            document.getElementById("t4_1").value = response["t4"]
            document.getElementById("t5_1").value = response["t5"]
            document.getElementById("t6_1").value = response["t6"]
            document.getElementById("m1_1").value = response["m1"]
            document.getElementById("m2_1").value = response["m2"]
            document.getElementById("m3_1").value = response["m3"]
            document.getElementById("m4_1").value = response["m4"]
            document.getElementById("m5_1").value = response["m5"]
            document.getElementById("m6_1").value = response["m6"]
            document.getElementById("l1_1").value = response["l1"]
            document.getElementById("l2_1").value = response["l2"]
            document.getElementById("l3_1").value = response["l3"]
            document.getElementById("l4_1").value = response["l4"]
            document.getElementById("l5_1").value = response["l5"]
            document.getElementById("l6_1").value = response["l6"]
            document.getElementById("n_1").value = response["lastCommandNumber"]
            document.getElementById("s_1").value = response["status"]
            document.getElementById("c_1").value = response["commandCounter"]
        }
    });
}

function get_data_robot_vacuum() {
    $.ajax({
        type: 'GET',
        url: '/robot_vacuum_connect',
        dataType: 'json',
        contentType: 'application/json',
        data: {},
        success: function (response) {
            document.getElementById("t1_2").value = response["t1"]
            document.getElementById("t2_2").value = response["t2"]
            document.getElementById("t3_2").value = response["t3"]
            document.getElementById("t4_2").value = response["t4"]
            document.getElementById("t5_2").value = response["t5"]
            document.getElementById("t6_2").value = response["t6"]
            document.getElementById("m1_2").value = response["m1"]
            document.getElementById("m2_2").value = response["m2"]
            document.getElementById("m3_2").value = response["m3"]
            document.getElementById("m4_2").value = response["m4"]
            document.getElementById("m5_2").value = response["m5"]
            document.getElementById("m6_2").value = response["m6"]
            document.getElementById("l1_2").value = response["l1"]
            document.getElementById("l2_2").value = response["l2"]
            document.getElementById("l3_2").value = response["l3"]
            document.getElementById("l4_2").value = response["l4"]
            document.getElementById("l5_2").value = response["l5"]
            document.getElementById("l6_2").value = response["l6"]
            document.getElementById("n_2").value = response["lastCommandNumber"]
            document.getElementById("s_2").value = response["status"]
            document.getElementById("c_2").value = response["commandCounter"]
        }
    });
}


function connect_traffic_lights() {
    $.ajax({
        type: 'GET',
        url: document.getElementById("URL_system").value + document.getElementById("traffic_lights_connect_URL").value,
        dataType: 'json',
        contentType: 'application/json',
        data: {},

        success: function (response) {
            if (response['L1'] == 1) {
                document.getElementById("traffic_blue").style.backgroundColor = 'blue'
            }
            else {
                document.getElementById("traffic_blue").style.backgroundColor = 'black'
            }
            if (response['L2'] == 1) {
                document.getElementById("traffic_red").style.backgroundColor = 'red'
            }
            else {
                document.getElementById("traffic_red").style.backgroundColor = 'black'
            }
            if (response['L3'] == 1) {
                document.getElementById("traffic_yellow").style.backgroundColor = 'yellow'
            }
            else {
                document.getElementById("traffic_yellow").style.backgroundColor = 'black'
            }
            if (response['L4'] == 1) {
                document.getElementById("traffic_green").style.backgroundColor = 'green'
            }
            else {
                document.getElementById("traffic_green").style.backgroundColor = 'black'
            }
        }
    });
}