from flask import Flask, jsonify, request, make_response
from model import Data

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/anggota', methods=['GET','POST','PUT','DELETE'])
def anggota():
    try:
        #panggil class model database
        dt = Data()
        values = ()
        
        #jika Method GET
        if request.method == 'GET':
            id_ = request.args.get("id")
            if id_:
                query = "SELECT * FROM anggota1 where id = %s "
                values = (id_,)
            else:
                query = "SELECT * FROM anggota1"
            data = dt.get_data(query, values)
        #jika Method POST
        elif request.method == 'POST':
            datainput = request.json
            nama = datainput['nama']
            pekerjaan = datainput['pekerjaan']
            usia = datainput['usia']
            
            query = "INSERT INTO anggota1 (nama, pekerjaan, usia) values (%s,%s,%s)"
            values = (nama, pekerjaan, usia)
            dt.insert_data(query, values)
            data = [{
                'pesan': 'berhasil menambah data'
            }]
        #jika Method PUT
        elif request.method == 'PUT':
            query = "UPDATE anggota1 SET id = %s "
            datainput = request.json
            id_ = datainput['id']
            values += (id_,)
            
            if 'nama' in datainput:
                nama = datainput['nama']
                values+= (nama, )
                query += ", nama = %s"
            if 'pekerjaan' in datainput:
                pekerjaan = datainput['pekerjaan']
                values += (pekerjaan, )
                query += ", pekerjaan = %s"
            if 'usia' in datainput:
                usia = datainput['usia']
                values+= (usia, )
                query += ", usia = %s"
            
            query += "where id = %s"
            values == (id_,)
            dt.insert_data(query, values)
            data = [{
                'pesan': 'berhasil mengubah data'
            }]
        #selain itu adalah DELETE, bila ada method selain keempat ini maka akan dipastikan error krna method tidak di assign
        else:
            query = "DELETE FROM anggota1 where id = %s "
            id_ = request.args.get("id")
            values = (id_,)
            dt.insert_data(query, values)
            data = [{
                'pesan': 'berhasil menghapus data'
            }]
    except Exception as e:
        return make_response(jsonify({'error': str(e)}), 400)
    return make_response(jsonify({'data': data}), 200)

app.run()