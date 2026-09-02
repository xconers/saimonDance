# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: AssetCheckout
def check_and_repair_data(records, max_age_days=365):
    """Проверяет целостность записей и 'чинит' очевидные проблемы.
    
    Исправляет:
      - записи с датой выдачи в будущем (сдвигает на 0 дней);
      - записи, где status == 'returned' но не указана дата возврата;
      - записи, где status == 'issued' но дата выдачи None;
      - записи, где status == 'pending' и дата выдачи больше, чем max_age_days от текущего дня.
    
    Возвращает список записей, которые были изменены (с флагом repaired=True).
    """
    repaired = []
    today = datetime.date.today()
    for rec in records:
        rec = dict(rec)
        if rec.get('repaired'):
            repaired.append(rec)
            continue
        
        status = rec.get('status', '')
        issued = rec.get('issued_date')
        returned = rec.get('returned_date')
        
        # Исправляем: status='issued' но дата выдачи None
        if status == 'issued' and not issued:
            rec['issued_date'] = today
            rec['status'] = 'issued'
            rec['repaired'] = True
            repaired.append(rec)
            continue
        
        # Исправляем: status='returned' но дата возврата None
        if status == 'returned' and not returned:
            rec['returned_date'] = today
            rec['repaired'] = True
            repaired.append(rec)
            continue
        
        # Исправляем: статус 'pending' и дата выдачи в будущем
        if status == 'pending' and issued:
            try:
                if issued > today:
                    rec['issued_date'] = today
                    rec['repaired'] = True
                    repaired.append(rec)
                    continue
            except TypeError:
                pass
        
        # Исправляем: статус 'pending' и дата выдачи слишком старая
        if status == 'pending' and issued:
            try:
                if (today - issued).days > max_age_days:
                    rec['status'] = 'returned'
                    rec['returned_date'] = today
                    rec['repaired'] = True
                    repaired.append(rec)
                    continue
            except TypeError:
                pass
        
        repaired.append(rec)
    return repaired
