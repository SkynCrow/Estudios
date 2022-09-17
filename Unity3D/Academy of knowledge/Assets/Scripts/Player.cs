using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Player : MonoBehaviour
{

    public float speed = 1;
    public float impulse = 1;
    public float rayDistance = 1;
    public float jumpCooldown = 1;

    private Rigidbody rgb;
    private bool canJump;
    private float jumpTimerCooldown;
    // Start is called before the first frame update
    void Awake()
    {
       rgb = GetComponent<Rigidbody>();
        jumpTimerCooldown = Time.time;
    }

    // Update is called once per frame
    void LateUpdate()
    {
        float h = (Input.GetAxis("Horizontal"));
        float v = (Input.GetAxis("Vertical"));

        transform.Translate(new Vector3(h,0,v) * speed);

        if (Input.GetKeyDown(KeyCode.Space) && canJump && Time.time > jumpTimerCooldown + jumpCooldown)
        {
            jumpTimerCooldown = Time.time;
            rgb.AddForce(transform.up * impulse,ForceMode.Impulse);
        }
        //if (Physics.Raycast(new Ray(transform.position,-transform.up),out RaycastHit hit, rayDistance))
        //{
        //    Debug.Log(hit.collider.name);
        //    if (hit.collider.name == "Floor")
        //        canJump = true;
        //    else
        //        canJump = false;
        //}
    }
    private void OnDrawGizmos()
    {
        Gizmos.DrawLine(transform.position,transform.position - transform.up * rayDistance);
    }

    private void OnCollisionEnter(Collision collision)
    {
        if (collision.transform.name == "Floor")
        {
            canJump = true;
        }
    }
    private void OnCollisionExit(Collision collision)
    {
        if (collision.transform.name == "Floor")
        {
            canJump = false;
        }
    }
}
