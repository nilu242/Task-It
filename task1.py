import csv


class Product:
    tax = 12
    output_file = 'task_1_output.csv'
    input_file = 'product_data.csv'
    output_header=['Product-Name', 'Product-CostPrice', 'Country', 'Product-SalesTax', 'Product-FinalPrice']

    def price_calculator(self,cost):
        return int(cost) + int(cost) *(self.tax/100)

    def product_read(self):
        with open(self.input_file) as csv_file:
            data=csv.reader(csv_file,delimiter=',')
            next(data)
            output_list=[]
            for row in data:
                    output_list.append([row[0],row[1],row[2],self.tax,self.price_calculator(row[1])])
            return output_list


    def product_write(self):
        result = self.product_read()
        with open(self.output_file,'w') as output:
            output_data=csv.writer(output)
            result.insert(0, self.output_header)
            output_data.writerows(result)

if __name__== "__main__":
    Product().product_write()
