import {
  Table,
  TableHeader,
  TableBody,
  TableColumn,
  TableRow,
  TableCell
} from "@nextui-org/table";
import axios from "axios";
import { useEffect, useState } from "react";

export default function UserTable() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const res = await axios.get("https://smile2step-ass.onrender.com/users");
      const data = await res.data;
      setUsers(data.users);
    };

    fetchData();
  }, []);

  return (
    <Table aria-label="Example static collection table">
      <TableHeader>
        <TableColumn>Name</TableColumn>
        <TableColumn>Email</TableColumn>
        <TableColumn>Dob</TableColumn>
      </TableHeader>
      <TableBody>
        {
            users.map((user) => (
                <TableRow key={user[0]}>
                <TableCell>{user[1]}</TableCell>
                <TableCell>{user[2]}</TableCell>
                <TableCell>{user[3]}</TableCell>
              </TableRow>
            ))
        }
       
      </TableBody>
    </Table>
  );
}
