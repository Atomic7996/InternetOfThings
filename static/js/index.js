setInterval(get_data_robot_gripper, 1000)
setInterval(get_data_robot_vacuum, 1000)
setInterval(connect_traffic_lights, 1000)
setInterval(get_data_barcode_scanner, 1000)
setInterval(get_data_control_panel, 1000)

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
        url: '/connect_trafficlight',
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

function get_data_barcode_scanner() {
    $.ajax({
        type: 'GET',
        url: '/connect_scanner',
        dataType: 'json',
        contentType: 'application/json',
        data: {},
        success: function (response) {
            document.getElementById("lastCode_4").value = response["lastCode"]
            document.getElementById("scanStatus_4").value = response["isScanning"] ? "1" : "0"
        }
    });
}

// ПАНЕЛЬ УПРАВЛЕНИЯ (ID 5)
function get_data_control_panel() {
    $.ajax({
        type: 'GET',
        url: '/connect_panel',
        dataType: 'json',
        contentType: 'application/json',
        data: {},
        success: function (response) {
            document.getElementById("switchMode_5").value = response["switchMode"]
            document.getElementById("button1Count_5").value = response["button1Count"]
            document.getElementById("button2Code_5").value = response["button2Code"]
            document.getElementById("button3Code_5").value = response["button3Code"]
            document.getElementById("lamp1_5").value = response["lamps"][0]
            document.getElementById("lamp2_5").value = response["lamps"][1]
            document.getElementById("lamp3_5").value = response["lamps"][2]
            document.getElementById("lamp4_5").value = response["lamps"][3]
        }
    });
}