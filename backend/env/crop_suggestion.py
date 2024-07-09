def suggest_crops(weather_data):
    temperature = weather_data.get('main', {}).get('temp')
    humidity = weather_data.get('main', {}).get('humidity')

    print(f"Temperature: {temperature}, Humidity: {humidity}")  
    suggestions = []

    if temperature is not None and humidity is not None:
        if temperature > 30 and humidity > 60 and humidity < 70:
            suggestions.extend([
                {
                    "name": "Cà chua",
                    "conditions": "Ấm áp và ẩm ướt",
                    "care": "Cây cần nắng nhiều và đất ẩm ướt. Thường thu hoạch sau khoảng 2-3 tháng.",
                    "harvest_time": "Thời gian thu hoạch vào mùa xuân và mùa hè.",
                    "fertilization": "Bón phân hữu cơ nhẹ nhàng vào đất trước khi trồng và thêm lần nữa sau khi cây phát triển được 3 tuần."
                },
                {
                    "name": "Dưa chuột",
                    "conditions": "Ấm và ẩm",
                    "care": "Cây thích hợp với đất sét, cần nhiều ánh sáng. Thu hoạch sau 50-70 ngày.",
                    "harvest_time": "Thu hoạch vào mùa hè.",
                    "fertilization": "Bón phân hữu cơ vào đất trước khi trồng và sau khi cây phát triển được 3 tuần."
                },
                {
                    "name": "Cà rốt",
                    "conditions": "Ấm và ẩm ướt",
                    "care": "Cây cần đất giàu dinh dưỡng và thoát nước tốt. Thu hoạch sau 70-80 ngày.",
                    "harvest_time": "Thu hoạch vào mùa thu và mùa đông.",
                    "fertilization": "Bón phân hữu cơ vào đất trước khi trồng và thêm vào 2-3 tuần sau khi trồng."
                },
                {
                    "name": "Bầu",
                    "conditions": "Ấm và ẩm",
                    "care": "Cây thích hợp với đất sét và nhiều nước. Thời gian thu hoạch từ 80-100 ngày.",
                    "harvest_time": "Thu hoạch vào mùa hè và mùa thu.",
                    "fertilization": "Bón phân hữu cơ vào đất trước khi trồng và thêm vào 4-5 tuần sau khi trồng."
                },
                {
                    "name": "Đậu xanh",
                    "conditions": "Ấm và ẩm ướt",
                    "care": "Cây cần đất sét và nhiều nước. Thu hoạch sau 60-80 ngày.",
                    "harvest_time": "Thu hoạch vào mùa hè và mùa thu.",
                    "fertilization": "Bón phân hữu cơ vào đất trước khi trồng và thêm vào 3-4 tuần sau khi trồng."
                }
            ])
        if temperature > 20 and temperature < 36 and humidity > 50 and humidity < 70:
            suggestions.extend([
                {
                    "name": "Rau diếp cá",
                    "conditions": "Mát và ẩm",
                    "care": "Cây yêu cầu nhiều nước và nắng nhẹ. Thời gian thu hoạch từ 30-40 ngày sau khi trồng.",
                    "harvest_time": "Có thể thu hoạch quanh năm.",
                    "fertilization": "Bón phân hữu cơ vào đất trước khi trồng và thêm vào 2-3 tuần sau khi trồng."
                },
                {
                    "name": "Cải bắp",
                    "conditions": "Mát và ẩm ướt",
                    "care": "Cây cần đất giàu dinh dưỡng và thoát nước tốt. Thu hoạch sau 6-8 tuần.",
                    "harvest_time": "Thu hoạch vào mùa thu và mùa đông.",
                    "fertilization": "Bón phân hữu cơ vào đất trước khi trồng và sau khi cây phát triển được 4 tuần."
                },
                {
                    "name": "Rau mồng tơi",
                    "conditions": "Mát và ẩm",
                    "care": "Cây cần đất giàu dinh dưỡng và thoát nước tốt. Thời gian thu hoạch từ 30-40 ngày.",
                    "harvest_time": "Có thể thu hoạch quanh năm.",
                    "fertilization": "Bón phân hữu cơ vào đất trước khi trồng và thêm vào 2-3 tuần sau khi trồng."
                },
                {
                    "name": "Cải thảo đỏ",
                    "conditions": "Mát và ẩm ướt",
                    "care": "Cây thích hợp với đất giàu dinh dưỡng và ẩm ướt. Thu hoạch sau 50-60 ngày.",
                    "harvest_time": "Thu hoạch vào mùa thu và mùa đông.",
                    "fertilization": "Bón phân hữu cơ vào đất trước khi trồng và thêm vào 3-4 tuần sau khi trồng."
                }
            ])
        if temperature > 30 and temperature < 40 and humidity >= 40 and humidity <= 60:
            suggestions.extend([
                {
                    "name": "Cây rau muống",
                    "conditions": "ấm và độ ẩm cao",
                    "care": "Rau muống cần nhiều nước và ánh sáng. Thời gian thu hoạch khoảng 25-30 ngày sau khi trồng.",
                    "harvest_time": "Có thể thu hoạch quanh năm.",
                    "fertilization": "Bón phân hữu cơ vào đất trước khi trồng và sau khi cây phát triển được 2-3 tuần."
                },
                {
                    "name": "Cây đậu bắp",
                    "conditions": "ấm và độ ẩm vừa phải",
                    "care": "Đậu bắp cần đất giàu dinh dưỡng và thoát nước tốt. Thu hoạch sau 50-60 ngày.",
                    "harvest_time": "Thu hoạch vào mùa hè và mùa thu.",
                    "fertilization": "Bón phân hữu cơ vào đất trước khi trồng và sau khi cây phát triển được 4 tuần."
                },
                {
                    "name": "Cây dưa leo",
                    "conditions": "ấm và độ ẩm cao",
                    "care": "Dưa leo cần đất giàu dinh dưỡng và thoát nước tốt. Thời gian thu hoạch từ 50-60 ngày.",
                    "harvest_time": "Có thể thu hoạch quanh năm.",
                    "fertilization": "Bón phân hữu cơ vào đất trước khi trồng và thêm vào 3-4 tuần sau khi trồng."
                },
                {
                    "name": "Cây cà chua",
                    "conditions": "ấm và độ ẩm vừa phải",
                    "care": "Cà chua cần đất giàu dinh dưỡng và thoát nước tốt. Thu hoạch sau 60-80 ngày.",
                    "harvest_time": "Thu hoạch vào mùa hè và mùa thu.",
                    "fertilization": "Bón phân hữu cơ vào đất trước khi trồng và sau khi cây phát triển được 4-6 tuần."
                }
            ])
        if temperature > 26  and humidity > 90:
            suggestions.extend([
                {
                    "name": "Rau diếp cá",
                    "conditions": "Mát và độ ẩm rất cao",
                    "care": "Cây yêu cầu nhiều nước và nắng nhẹ. Thời gian thu hoạch từ 30-40 ngày sau khi trồng.",
                    "harvest_time": "Có thể thu hoạch quanh năm.",
                    "fertilization": "Bón phân hữu cơ vào đất trước khi trồng và thêm vào 2-3 tuần sau khi trồng."
                },
                {
                    "name": "Cà chua",
                    "conditions": "Ấm áp và ẩm ướt",
                    "care": "Cây cần nắng nhiều và đất ẩm ướt. Thường thu hoạch sau khoảng 2-3 tháng.",
                    "harvest_time": "Thời gian thu hoạch vào mùa xuân và mùa hè.",
                    "fertilization": "Bón phân hữu cơ nhẹ nhàng vào đất trước khi trồng và thêm lần nữa sau khi cây phát triển được 3 tuần."
                },
                {
                    "name": "Bầu",
                    "conditions": "Ấm và ẩm",
                    "care": "Cây thích hợp với đất sét và nhiều nước. Thời gian thu hoạch từ 80-100 ngày.",
                    "harvest_time": "Thu hoạch vào mùa hè và mùa thu.",
                    "fertilization": "Bón phân hữu cơ vào đất trước khi trồng và thêm vào 4-5 tuần sau khi trồng."
                },
                {
                    "name": "Cây đậu xanh",
                    "conditions": "Ấm và ẩm ướt",
                    "care": "Cây cần đất sét và nhiều nước. Thu hoạch sau 60-80 ngày.",
                    "harvest_time": "Thu hoạch vào mùa hè và mùa thu.",
                    "fertilization": "Bón phân hữu cơ vào đất trước khi trồng và thêm vào 3-4 tuần sau khi trồng."
                }
            ])
        if temperature > 25 and temperature > 32 and humidity > 35 and humidity < 42:
            suggestions.extend([
                {
                    "name": "Cây ớt",
                    "conditions": "Mát và độ ẩm vừa phải",
                    "care": "Ớt cần đất thoát nước tốt và ánh sáng đầy đủ. Thời gian thu hoạch từ 60-90 ngày.",
                    "harvest_time": "Có thể thu hoạch quanh năm.",
                    "fertilization": "Bón phân hữu cơ vào đất trước khi trồng và sau khi cây phát triển được 4-6 tuần."
                },
                {
                    "name": "Cây cải bó xôi",
                    "conditions": "Mát và độ ẩm vừa phải",
                    "care": "Cải bó xôi cần đất giàu dinh dưỡng và thoát nước tốt. Thu hoạch sau 40-50 ngày.",
                    "harvest_time": "Thu hoạch vào mùa xuân và mùa thu.",
                    "fertilization": "Bón phân hữu cơ vào đất trước khi trồng và sau khi cây phát triển được 2-3 tuần."
                },
                {
                    "name": "Cây bầu",
                    "conditions": "Mát và độ ẩm vừa phải",
                    "care": "Bầu cần đất giàu dinh dưỡng và thoát nước tốt. Thời gian thu hoạch từ 70-80 ngày.",
                    "harvest_time": "Có thể thu hoạch quanh năm.",
                    "fertilization": "Bón phân hữu cơ vào đất trước khi trồng và thêm vào 3-4 tuần sau khi trồng."
                },
                {
                    "name": "Cây bí đỏ",
                    "conditions": "Mát và độ ẩm vừa phải",
                    "care": "Bí đỏ cần đất giàu dinh dưỡng và thoát nước tốt. Thu hoạch sau 80-100 ngày.",
                    "harvest_time": "Thu hoạch vào mùa hè và mùa thu.",
                    "fertilization": "Bón phân hữu cơ vào đất trước khi trồng và sau khi cây phát triển được 4-6 tuần."
                }
            ])

        if temperature > 20 and temperature < 25 and humidity > 25 and humidity < 35:
            suggestions.extend([
                {
                    "name": "Cây cà tím",
                    "conditions": "Nhiệt độ thấp và độ ẩm thấp",
                    "care": "Cà tím cần đất thoát nước tốt và ánh sáng đầy đủ. Thời gian thu hoạch từ 70-90 ngày.",
                    "harvest_time": "Có thể thu hoạch quanh năm.",
                    "fertilization": "Bón phân hữu cơ vào đất trước khi trồng và sau khi cây phát triển được 4-6 tuần."
                },
                {
                    "name": "Cây rau mồng tơi",
                    "conditions": "Nhiệt độ thấp và độ ẩm thấp",
                    "care": "Rau mồng tơi cần đất giàu dinh dưỡng và thoát nước tốt. Thu hoạch sau 30-40 ngày.",
                    "harvest_time": "Thu hoạch vào mùa xuân và mùa thu.",
                    "fertilization": "Bón phân hữu cơ vào đất trước khi trồng và sau khi cây phát triển được 2-3 tuần."
                },
                {
                    "name": "Cây mướp",
                    "conditions": "Nhiệt độ thấp và độ ẩm thấp",
                    "care": "Mướp cần đất giàu dinh dưỡng và thoát nước tốt. Thời gian thu hoạch từ 50-60 ngày.",
                    "harvest_time": "Có thể thu hoạch quanh năm.",
                    "fertilization": "Bón phân hữu cơ vào đất trước khi trồng và thêm vào 3-4 tuần sau khi trồng."
                },
                {
                    "name": "Cây đậu bắp",
                    "conditions": "Nhiệt độ thấp và độ ẩm thấp",
                    "care": "Đậu bắp cần đất giàu dinh dưỡng và thoát nước tốt. Thu hoạch sau 50-60 ngày.",
                    "harvest_time": "Thu hoạch vào mùa hè và mùa thu.",
                    "fertilization": "Bón phân hữu cơ vào đất trước khi trồng và sau khi cây phát triển được 4-6 tuần."
                }
            ])
        if temperature > 15 and temperature < 20  and humidity > 65:
            suggestions.extend([
                {
                    "name": "Cây cà tím",
                    "conditions": "Lạnh và độ ẩm cao",
                    "care": "Cà tím cần đất thoát nước tốt và ánh sáng đầy đủ. Thời gian thu hoạch từ 70-90 ngày.",
                    "harvest_time": "Có thể thu hoạch quanh năm.",
                    "fertilization": "Bón phân hữu cơ vào đất trước khi trồng và sau khi cây phát triển được 4-6 tuần."
                },
                {
                    "name": "Cây rau mồng tơi",
                    "conditions": "Lạnh và độ ẩm cao",
                    "care": "Rau mồng tơi cần đất giàu dinh dưỡng và thoát nước tốt. Thu hoạch sau 30-40 ngày.",
                    "harvest_time": "Thu hoạch vào mùa xuân và mùa thu.",
                    "fertilization": "Bón phân hữu cơ vào đất trước khi trồng và sau khi cây phát triển được 2-3 tuần."
                },
                {
                    "name": "Cây mướp",
                    "conditions": "Lạnh và độ ẩm cao",
                    "care": "Mướp cần đất giàu dinh dưỡng và thoát nước tốt. Thời gian thu hoạch từ 50-60 ngày.",
                    "harvest_time": "Có thể thu hoạch quanh năm.",
                    "fertilization": "Bón phân hữu cơ vào đất trước khi trồng và thêm vào 3-4 tuần sau khi trồng."
                },
                {
                    "name": "Cây đậu bắp",
                    "conditions": "Lạnh và độ ẩm cao",
                    "care": "Đậu bắp cần đất giàu dinh dưỡng và thoát nước tốt. Thu hoạch sau 50-60 ngày.",
                    "harvest_time": "Thu hoạch vào mùa hè và mùa thu.",
                    "fertilization": "Bón phân hữu cơ vào đất trước khi trồng và sau khi cây phát triển được 4-6 tuần."
                }
            ])

    return suggestions
