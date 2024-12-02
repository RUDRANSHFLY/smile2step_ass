import { Button } from "@nextui-org/button";
import {CircularProgress} from "@nextui-org/progress";
import { DatePicker } from "@nextui-org/date-picker";
import {
  Modal,
  ModalContent,
  ModalHeader,
  ModalBody,
  ModalFooter,
  useDisclosure
} from "@nextui-org/modal";
import { Input } from "@nextui-org/input";
import { useRef, useState } from "react";
import axios from "axios";
import { toast } from "alert";

const UserModal = () => {
  const { isOpen, onOpenChange, onOpen } = useDisclosure();
  const [loading, setLoading] = useState(false);
  const userNameRef = useRef();
  const [dob, setDob] = useState();
  const emailRef = useRef();

  const onRegister = async () => {
    setLoading(true);
    const username = userNameRef.current.value;
    const email = emailRef.current.value;
    

    const promise = axios
      .post("https://smile2step-ass.onrender.com/user", {
        username,
        email,
        dob
      })
      .then((data) => {
        if (data.status === 201) {
          toast.success("User created");
        }
      })
      .catch((err) => {
        toast.error(err.response.data.error);
      }).finally(() => {
        setLoading(false)
      });


    return;
  };

  return (
    <>
        {
            loading && <CircularProgress color="danger" aria-label="Loading..."/>

        }
      <Button onPress={onOpen}>Add User</Button>
      <Modal isOpen={isOpen} onOpenChange={onOpenChange}>
        <ModalContent>
          {(onClose) => (
            <>
              <ModalHeader className="flex flex-col gap-1">
                Add a new user
              </ModalHeader>
              <ModalBody>
                <div className="flex flex-col w-full flex-wrap md:flex-nowrap gap-4">
                  <Input type="text" label="User Name" ref={userNameRef} />
                  <Input type="email" label="Email" ref={emailRef} />
                  <DatePicker
                    label="Birth date"
                    className="max-w-[284px]"
                    onChange={(date) => {
                      const day = date.day;
                      const month = date.month;
                      const year = date.year;
                      const dateStr = `${year}-${month}-${day}`;
                      setDob(dateStr);
                    }}
                  />
                </div>
              </ModalBody>
              <ModalFooter>
                <Button color="danger" variant="light" onPress={onClose}>
                  Close
                </Button>
                <Button
                  color="primary"
                  onPress={async () => {
                    await onRegister();
                    onClose();
                  }}
                >
                  Register
                </Button>
              </ModalFooter>
            </>
          )}
        </ModalContent>
      </Modal>
    </>
  );
};

export default UserModal;
