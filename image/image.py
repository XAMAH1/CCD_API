from flask import request, jsonify, send_file

def send_image():
    ff = ["main.rar", "Hide-False.rar", "Hide-False0.0.1v.rar"]
    filenum = request.args.get('filenum')
    return send_file(f"C:\\Users\\Admin\\Desktop\\ttt\\{ff[int(filenum)]}", as_attachment=True)

    #filenum = request.args.get('filenum')
    #file = ["autme_server.png", "bank.png", "ekx.png", "gl_menu.png", "img.png", "loading_server.png",
    #        "loading_server_procces.png", "perevod.png", "prochent.png", "reconnect.png",
    #        "register.png", "register_sogl.png", "server_vibor.png", "snatie.png"
    #        ]
    #path = "C:\\Users\\Admin\\PycharmProjects\\CCD_API_new\\image\\photo\\"

    #if not filenum:
    #    return jsonify({'error': 'Ошибка, такого фота нет на сервере'}), 200

    #try:
     #   return send_file("C:\\Users\\Admin\\PycharmProjects\\CCD_API_new\\image\\photo\\"+file[int(filenum)], as_attachment=True)
    #except FileNotFoundError:
    #    return jsonify({'error': 'Файл не найден'}), 404