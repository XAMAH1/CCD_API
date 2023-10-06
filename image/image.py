from flask import request, jsonify, send_file

def send_image():
    filenum = request.args.get('filenum')
    file = ["autme_server.png", "bank.png", "ekx.png", "gl_menu.png", "img.png", "loading_server.png",
            "loading_server_procces.png", "perevod.png", "prochent.png", "reconnect.png",
            "register.png", "register_sogl.png", "server_vibor.png", "snatie.png"
            ]
    path = "C:\\Users\\Admin\\PycharmProjects\\CCD_API_new\\image\\photo\\"

    if not filenum:
        return jsonify({'error': 'Ошибка, такого фота нет на сервере'}), 400

    try:
        return send_file(path+file[int(filenum)], as_attachment=True)
    except FileNotFoundError:
        return jsonify({'error': 'Файл не найден'}), 404